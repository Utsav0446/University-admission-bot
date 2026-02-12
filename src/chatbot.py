PROGRAM_ALIASES = {
    "cse": "MS Computer Science",
    "computer science": "MS Computer Science",
    "cs": "MS Computer Science",
    "mba": "MBA"
}

def get_response(user_query, admission_data):
    query = user_query.lower()
    selected_program = None

    for alias, program in PROGRAM_ALIASES.items():
        if alias in query:
            selected_program = program
            break

    if not selected_program:
        return "❗ Please mention a valid program like CSE, CS, or MBA."

    info = admission_data[selected_program]

    response = f"""
🎓 **{selected_program} – Admission Overview**

✅ **Eligibility:**  
{info['eligibility']}

📄 **Required Documents:**  
{', '.join(info['documents'])}

⏰ **Application Deadline:**  
{info['deadline']}

💡 *You can also ask:*  
- Is GRE required?  
- Can non-CS students apply?  
- Is work experience mandatory?
"""
    return response