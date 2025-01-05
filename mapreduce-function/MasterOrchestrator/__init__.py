import azure.durable_functions as df


async def orchestrator_function(context: df.DurableOrchestrationContext):
    # Step 1: Fetch input data
    input_data = await context.call_activity("GetInputDataFn", None)

    # Step 2: Map phase (fan-out)
    map_tasks = [
        context.call_activity("Mapper", (i, line)) for i, line in enumerate(input_data)
    ]
    map_results = await context.task_all(map_tasks)

    # Step 3: Shuffle phase
    shuffled_data = await context.call_activity("Shuffler", map_results)

    # Step 4: Reduce phase (fan-out)
    reduce_tasks = [
        context.call_activity("Reducer", (word, counts))
        for word, counts in shuffled_data.items()
    ]
    final_results = await context.task_all(reduce_tasks)

    # Step 5: Return results
    return final_results


main = df.Orchestrator.create(orchestrator_function)
