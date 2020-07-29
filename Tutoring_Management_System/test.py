class Subject():
    def __init__(self, subjectName):
        #self.subjectId = getNewId("subject_id","Subjects")
        self.subjectName = subjectName
    
    def commitSubject(self):
        with closing(conn.cursor()) as c:
         query = '''INSERT INTO "main"."Subjects"("subject_name") 
                    VALUES (?);'''
         c.execute(query,(self.subjectName,))
         conn.commit()
    
    def __str__(self):
        output = "{} | {}".format(self.subjectId,self.subjectName)
        return output

x = Subject('Math')
print(x.__str__())