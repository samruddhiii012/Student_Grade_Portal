import streamlit as st
import os

# ---- APP SETUP ----
st.set_page_config(page_title="Student Portal")
st.title("Student Grade System")

# --- STEP 1: INPUT SECTION ---
st.header("Enter Student Details")
name = st.text_input("Student Name:")
n = st.number_input("Number of Subjects:", min_value=1, step=1, value=1)

marks = []
st.write("Enter Marks For Each Subject:")
for i in range(int(n)):      # Each input box needs a unique key, so we use i
    m = st.number_input(f"Subject {i + 1}", min_value=0, max_value=100, key=i)
    marks.append(m)

# --- STEP 2: CALCULATION & SAVING ---
if st.button("Calculate & Save Record"):
    if name != "":
        # Your original logic
        total = sum(marks)
        average = total / n

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        # Display current result
        st.success(f"Done! {name} got Grade: {grade}")
        st.success("Record Saved Successfully!")
        
        # Save to a text file (The "Database")
        # format: Name | Total | Average | Grade
        with open("records.txt", "a") as f:
            f.write(f"{name} | Total: {total} | Avg: {average:.2f} | Grade: {grade}\n")
    else:
        st.error("Please enter a student name first!")

# --- STEP 3: VIEW & MANAGE DATA ---
st.sidebar.header("Saved Records History")

if os.path.exists("records.txt"):
    # 1. READ: We now read the file line by line into a list
    with open("records.txt", "r") as f:
        lines = f.readlines()
    
    # 2. DISPLAY: We loop through the list to show each student
    for line in lines:
        st.sidebar.text(line.strip())

    st.sidebar.divider()

    # 3. NEW BUTTON: Logic to remove only the last entry
    if st.sidebar.button("Delete Last Entry"):
        if lines:
            lines.pop()  # This removes the last student from the list
            with open("records.txt", "w") as f: # "w" clears the file to overwrite it
                f.writelines(lines) # Saves the list back without the deleted student
            st.rerun() # Refreshes the app to show the change

    # 4. YOUR ORIGINAL BUTTON: Wipes everything
    if st.sidebar.button("Clear All Records"):
        os.remove("records.txt")
        st.rerun()
else:
    st.sidebar.write("No records saved yet.")
