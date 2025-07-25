import importlib


def execute_plan(plan: list, user_context: dict) -> dict:
    """
    Executes a list of tasks from a plan.

    Args:
        plan: A list of task dictionaries from the planner.
        user_context: A dictionary to pass results from one step to another.

    Returns:
        A dictionary containing the results of all executed tasks.
    """
    print("\n--- EXECUTOR: Starting plan execution ---")
    all_results = {}

    for task in plan:
        agent_name = task['agent']
        task_name = task['task']
        params = task.get('params', {})

        for p_key, p_value in params.items():
            if isinstance(p_value, str) and p_value in user_context:
                params[p_key] = user_context[p_value]

        print(
            f"EXECUTOR: Running task '{task_name}' for agent '{agent_name}' with params: {params}")

        try:
            agent_module = importlib.import_module(f"agents.{agent_name}")
            task_function = getattr(agent_module, task_name)
            result = task_function(**params)
            all_results[task_name] = result

            # THE FIX IS HERE: This now matches the real task name.
            if task_name == 'find_available_venues':
                user_context['available_venues'] = result

        except Exception as e:
            print(f"❌ EXECUTOR: Failed to run task '{task_name}'. Error: {e}")
            all_results[task_name] = {"error": str(e)}

    print("--- EXECUTOR: Plan execution complete ---")
    return all_results
