class studentinfo:
    stid=204
    stnm="bharti"

    def getdata(self):
        print("student ID:",self.stid)
        print("student name:",self.stnm)
st=studentinfo() #object
st.getdata()
st.stid=206
st.stnm="shivansh"
st.getdata()

#instance
studentinfo().getdata()
studentinfo().stid=2312
studentinfo().stnm="princy"
studentinfo().getdata()