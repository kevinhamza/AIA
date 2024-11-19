import unittest
from unittest.mock import patch
from modules.automation import TaskAutomation

class TestTaskAutomationModule(unittest.TestCase):

    def setUp(self):
        self.task_automation = TaskAutomation()

    @patch('modules.automation.subprocess.run')
    def test_execute_task(self, mock_run):
        # Simulate executing a task via subprocess
        mock_run.return_value = "Task executed successfully"

        result = self.task_automation.execute_task("run_task.sh")

        # Verify that the task execution is successful
        self.assertEqual(result, "Task executed successfully")
        mock_run.assert_called_once_with(["bash", "run_task.sh"])

    @patch('modules.automation.subprocess.run')
    def test_handle_task_execution_error(self, mock_run):
        # Simulate an error during task execution
        mock_run.side_effect = Exception("Task execution failed")

        with self.assertRaises(Exception):
            self.task_automation.execute_task("invalid_task.sh")

    @patch('modules.automation.subprocess.run')
    def test_execute_multiple_tasks(self, mock_run):
        # Simulate executing multiple tasks
        mock_run.side_effect = ["Task 1 executed", "Task 2 executed"]

        tasks = ["task1.sh", "task2.sh"]
        results = self.task_automation.execute_multiple_tasks(tasks)

        # Verify that all tasks were executed
        self.assertEqual(results, ["Task 1 executed", "Task 2 executed"])
        mock_run.assert_any_call(["bash", "task1.sh"])
        mock_run.assert_any_call(["bash", "task2.sh"])

if __name__ == '__main__':
    unittest.main()
