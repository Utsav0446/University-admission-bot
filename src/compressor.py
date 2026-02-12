def compress_program_info(program_data):
    summary = []
    summary.append(f"Eligibility: {program_data['eligibility']}")
    summary.append(f"Deadline: {program_data['deadline']}")
    summary.append(f"Documents Required: {', '.join(program_data['documents'])}")
    return "\n".join(summary)