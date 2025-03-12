import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations=examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
    allrows=students.merge(subjects,how='cross')
    df=allrows.merge(examinations,how='left',on=('student_id','subject_name'))
    df['attended_exams']=df['attended_exams'].fillna(0)
    return df.sort_values(by=['student_id','subject_name'])