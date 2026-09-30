import time
from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import RunLifeCycleState, RunResultState


@dag
def orchestrate():

    @task
    def ingest_cdc():
        ws = WorkspaceClient(host="your_databricks_host", token="your_databricks_token")

        job_trigger = ws.jobs.run_now(job_id=116508741272036)
        # print(job_trigger)

        while True:

            job_run = ws.jobs.get_run(job_trigger.run_id)

            if job_run.state.life_cycle_state in [
                RunLifeCycleState.TERMINATED,
                RunLifeCycleState.SKIPPED,
                RunLifeCycleState.INTERNAL_ERROR,
            ]:
                if job_run.state.result_state == RunResultState.SUCCESS:
                    print("Job Completed Successfully")
                    break
                else:
                    raise Exception(
                        f"Job failed with state:{job_run.state.result_state}"
                    )

            time.sleep(5)  # Wait for 5 seconds before checking the job status

        return "CDC Ingestion Completed"

    @task.bash
    def clean_target():
        return "rm -rf /opt/airflow_setup/supermart_project/target && rm -rf /opt/airflow_setup/supermart_project/logs"

    @task.bash
    def source_freshness_check():
        # Manually set the working directory using the 'cd' command before executing the Python script
        return "cd /opt/airflow_setup/supermart_project && dbt source freshness"

    # source_freshness_check_task = BashOperator(
    #     task_id="source_freshness_check",
    #     cwd="/opt/airflow_setup/supermart_project",
    #     bash_command="dbt source freshness",
    # )

    silver_technical = BashOperator(
        task_id="silver_technical",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt run --select silver_tech",
    )

    silver_technical_tests = BashOperator(
        task_id="silver_technical_tests",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt test --select silver_tech",
    )

    silver_business = BashOperator(
        task_id="silver_business",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt run --select silver_business",
    )

    silver_business_tests = BashOperator(
        task_id="silver_business_tests",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt test --select silver_business",
    )

    gold_ephemeral = BashOperator(
        task_id="gold_ephemeral",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt run --select gold/ephemeral",
    )

    gold_dimensions = BashOperator(
        task_id="gold_dimensions",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt snapshot",
    )

    gold_facts = BashOperator(
        task_id="gold_facts",
        cwd="/opt/airflow_setup/supermart_project",
        bash_command="dbt run --select gold/fact",
    )

    (
        ingest_cdc()
        >> clean_target()
        >> source_freshness_check()
        >> silver_technical
        >> silver_technical_tests
        >> silver_business
        >> silver_business_tests
        >> gold_ephemeral
        >> gold_dimensions
        >> gold_facts
    )


orchestrate_dag = orchestrate()
