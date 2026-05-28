# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from visualization.chart import stack_bar_1,stack_bar_2,stack_bar_3,stack_bar_4,stack_bar_5,stack_bar_6
from visualization.pr_chart import scatter_1,scatter_2,scatter_3,scatter_4,scatter_5,scatter_6
from visualization.per_chart import pie_chart_1,pie_chart_2,pie_chart_3,pie_chart_4,pie_chart_5,pie_chart_6
from visualization.th_stud import th_sd_1,th_sd_2,th_sd_3,th_sd_4,th_sd_5,th_sd_6
from visualization.all_marks import all_mk_1,all_mk_2,all_mk_3,all_mk_4,all_mk_5,all_mk_6
from visualization.line_chart import line_c
from visualization.f_teach import front_1
from visualization.th_bh import bar_bh_1,bar_bh_3,bar_bh_6
from visualization.th_pt import bar_pt_5,bar_pt_6
from visualization.th_rt import bar_rt_2,bar_rt_3,bar_rt_4,bar_rt_5,bar_rt_6
from visualization.th_sk import bar_sk_3,bar_sk_6
from visualization.cmp_chart import cmp_1,cmp_2,cmp_3,cmp_4,cmp_5,cmp_6
from visualization.fail import fail_1,fail_2,fail_3,fail_4,fail_5,fail_6
from visualization.stud_login import validate_stud_login
from visualization.teach_login import validate_teach_login


app = Flask(__name__)
app.secret_key = 'session_secret_key'  # Set a secret key for session management


@app.route('/')
def home():
    return render_template('index.html')
#----------------------------------- student login----------------------------------- 
@app.route('/stud_login', methods=['GET', 'POST'])
def stud_login():
    if request.method == 'POST':
        enrollment = request.form['enrollment']
        password = request.form['password']
        user_info = validate_stud_login(enrollment, password)
        if user_info:
            student_name = user_info.get('student_name')

            if student_name:
                session['enrollment'] = enrollment
                session['student_name'] = student_name
                return redirect(url_for('stud'))  # Redirect to the 'stud' route
            else:
                return 'Invalid user type'

        return 'Invalid username or password'

    return render_template('stud_login.html')
#----------------------------------- teacher login----------------------------------- 
@app.route('/teach_login', methods=['GET', 'POST'])
def teach_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_info = validate_teach_login(username, password)
        if user_info:
            teacher_name = user_info.get('teacher_name')
            user_type = user_info.get('user_type')  # Assuming 'user_type' is returned by validate_teach_login

            if user_type == 'HOD':
                session['teacher_name'] = teacher_name
                return redirect(url_for('teach'))
            elif teacher_name == 'Mr. C.P.Bhamare':
                session['teacher_name'] = teacher_name
                return redirect(url_for('teach_bh'))
            elif teacher_name == 'Mr.N.D.Patel':
                session['teacher_name'] = teacher_name
                return redirect(url_for('teach_pt'))
            elif teacher_name == 'Ms.R.S.Patil':
                session['teacher_name'] = teacher_name
                return redirect(url_for('teach_rt'))
            elif teacher_name == 'Ms. S.H.Patil':
                session['teacher_name'] = teacher_name
                return redirect(url_for('teach_sk'))
            else:
                return 'Invalid user type'

        return 'Invalid username or password'

    return render_template('teach_login.html')    
#----------------------------------- after login----------------------------------- 
@app.route('/stud')
def stud():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        line_html1,stud_name = line_c(enrollment)
        return render_template('stud.html', student_name=student_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'

@app.route('/teach/')
def teach():
    teacher_name=session.get('teacher_name')
    front_html1 = front_1()
    return render_template('teach.html',teacher_name=teacher_name,front_html1=front_html1)

@app.route('/teach_bh')
def teach_bh():
    teacher_name=session.get('teacher_name')
    front_html1 = front_1()
    return render_template('teach_bh.html',teacher_name=teacher_name,front_html1=front_html1)

@app.route('/teach_pt')
def teach_pt():
    teacher_name=session.get('teacher_name')
    front_html1 = front_1()
    return render_template('teach_pt.html',teacher_name=teacher_name,front_html1=front_html1)

@app.route('/teach_rt')
def teach_rt():
    teacher_name=session.get('teacher_name')
    front_html1 = front_1()
    return render_template('teach_rt.html',teacher_name=teacher_name,front_html1=front_html1)

@app.route('/teach_sk')
def teach_sk():
    teacher_name=session.get('teacher_name')
    front_html1 = front_1()
    return render_template('teach_sk.html',teacher_name=teacher_name,front_html1=front_html1)



#----------------------------------------------TEACHER----------------------------------------------
@app.route('/pr_teachyr1')
def pr_teachyr1():
    teacher_name=session.get('teacher_name')
    pr_html1 = scatter_1()
    pr_html2 = scatter_2()
    return render_template('pr_teachyr1.html',teacher_name=teacher_name,pr_html1=pr_html1,pr_html2=pr_html2)

@app.route('/pr_teachyr2')
def pr_teachyr2():
    teacher_name=session.get('teacher_name')
    pr_html3 = scatter_3()
    pr_html4 = scatter_4()
    return render_template('pr_teachyr2.html',teacher_name=teacher_name,pr_html3=pr_html3,pr_html4=pr_html4)

@app.route('/pr_teachyr3')
def pr_teachyr3():
    teacher_name=session.get('teacher_name')
    pr_html5 = scatter_5()
    pr_html6 = scatter_6()
    return render_template('pr_teachyr3.html',teacher_name=teacher_name,pr_html5=pr_html5,pr_html6=pr_html6)

@app.route('/teachyr1')
def teachyr1():
    teacher_name=session.get('teacher_name')
    chart_html1 = stack_bar_1()
    chart_html2 = stack_bar_2()
    return render_template('teachyr1.html',teacher_name=teacher_name,chart_html1=chart_html1,chart_html2=chart_html2)

@app.route('/teachyr2')
def teachyr2():
    teacher_name=session.get('teacher_name')
    chart_html3 = stack_bar_3()
    chart_html4 = stack_bar_4()
    return render_template('teachyr2.html',teacher_name=teacher_name,chart_html3=chart_html3,chart_html4=chart_html4)

@app.route('/teachyr3')
def teachyr3():
    teacher_name=session.get('teacher_name')
    chart_html5 = stack_bar_5()
    chart_html6 = stack_bar_6()
    return render_template('teachyr3.html',teacher_name=teacher_name,chart_html5=chart_html5,chart_html6=chart_html6)

@app.route('/all_teachyr1')
def all_teachyr1():
    teacher_name=session.get('teacher_name')
    all_html1 = all_mk_1()
    all_html2 = all_mk_2()
    return render_template('all_teachyr1.html',teacher_name=teacher_name,all_html1=all_html1,all_html2=all_html2)

@app.route('/all_teachyr2')
def all_teachyr2():
    teacher_name=session.get('teacher_name')
    all_html3 = all_mk_3()
    all_html4 = all_mk_4()
    return render_template('all_teachyr2.html',teacher_name=teacher_name,all_html3=all_html3,all_html4=all_html4)

@app.route('/all_teachyr3')
def all_teachyr3():
    teacher_name=session.get('teacher_name')
    all_html5 = all_mk_5()
    all_html6 = all_mk_6()
    return render_template('all_teachyr3.html',teacher_name=teacher_name,all_html5=all_html5,all_html6=all_html6)

@app.route('/sp_teach', methods=['GET', 'POST'])
def sp_teach():
    teacher_name=session.get('teacher_name')
    enroll_value = request.form['enroll']
    if enroll_value:
        line_html1,stud_name = line_c(enroll_value)
        return render_template('sp_teach.html',teacher_name=teacher_name ,student_name=stud_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'
    
@app.route('/fail_teachyr1')
def fail_teachyr1():
    teacher_name=session.get('teacher_name')
    fail_html1=fail_1()
    fail_html2=fail_2()
    return render_template('fail_teachyr1.html',teacher_name=teacher_name,fail_html1=fail_html1,fail_html2=fail_html2)

@app.route('/fail_teachyr2')
def fail_teachyr2():
    teacher_name=session.get('teacher_name')
    fail_html3=fail_3()
    fail_html4=fail_4()
    return render_template('fail_teachyr2.html',teacher_name=teacher_name,fail_html3=fail_html3,fail_html4=fail_html4)

@app.route('/fail_teachyr3')
def fail_teachyr3():
    teacher_name=session.get('teacher_name')
    fail_html5=fail_5()
    fail_html6=fail_6()
    return render_template('fail_teachyr3.html',teacher_name=teacher_name,fail_html5=fail_html5,fail_html6=fail_html6)

    
#----------------------------------------------SUBJECT TEACHER----------------------------------------------

@app.route('/th_bh')
def th_bh():
    teacher_name=session.get('teacher_name')
    th_bh_html1=bar_bh_1()
    th_bh_html3=bar_bh_3()
    th_bh_html6=bar_bh_6()
    return render_template('th_bh.html',teacher_name=teacher_name,th_bh_html1=th_bh_html1,th_bh_html3=th_bh_html3,th_bh_html6=th_bh_html6)

@app.route('/sp_bh', methods=['GET', 'POST'])
def sp_bh():
    teacher_name=session.get('teacher_name')
    enroll_value = request.form['enroll']
    if enroll_value:
        line_html1,stud_name = line_c(enroll_value)
        return render_template('sp_bh.html',teacher_name=teacher_name ,student_name=stud_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'
    
@app.route('/th_pt')
def th_pt():
    teacher_name=session.get('teacher_name')
    th_pt_html5=bar_pt_5()
    th_pt_html6=bar_pt_6()
    return render_template('th_pt.html',teacher_name=teacher_name,th_pt_html5=th_pt_html5,th_pt_html6=th_pt_html6)

@app.route('/sp_pt', methods=['GET', 'POST'])
def sp_pt():
    teacher_name=session.get('teacher_name')
    enroll_value = request.form['enroll']
    if enroll_value:
        line_html1,stud_name = line_c(enroll_value)
        return render_template('sp_pt.html',teacher_name=teacher_name ,student_name=stud_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'
    
@app.route('/th_rt')
def th_rt():
    teacher_name=session.get('teacher_name')
    th_rt_html2=bar_rt_2()
    th_rt_html3=bar_rt_3()
    th_rt_html4=bar_rt_4()
    th_rt_html5=bar_rt_5()
    th_rt_html6=bar_rt_6()
    return render_template('th_rt.html',teacher_name=teacher_name,th_rt_html2=th_rt_html2,th_rt_html3=th_rt_html3,th_rt_html4=th_rt_html4,th_rt_html5=th_rt_html5,th_rt_html6=th_rt_html6)

@app.route('/sp_rt', methods=['GET', 'POST'])
def sp_rt():
    teacher_name=session.get('teacher_name')
    enroll_value = request.form['enroll']
    if enroll_value:
        line_html1,stud_name = line_c(enroll_value)
        return render_template('sp_rt.html',teacher_name=teacher_name ,student_name=stud_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'

@app.route('/th_sk')
def th_sk():
    teacher_name=session.get('teacher_name')
    th_sk_html3=bar_sk_3()
    th_sk_html6=bar_sk_6()
    return render_template('th_sk.html',teacher_name=teacher_name,th_sk_html3=th_sk_html3,th_sk_html6=th_sk_html6)

@app.route('/sp_sk', methods=['GET', 'POST'])
def sp_sk():
    teacher_name=session.get('teacher_name')
    enroll_value = request.form['enroll']
    if enroll_value:
        line_html1,stud_name = line_c(enroll_value)
        return render_template('sp_sk.html',teacher_name=teacher_name ,student_name=stud_name, line_html1=line_html1)
    else:
        return 'Enrollment not found in session'
   
    
#----------------------------------------------STUDENT----------------------------------------------
@app.route('/per_studyr1/')
def per_studyr1():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        per_html1,per_src1 = pie_chart_1(enrollment)  # Pass enrollment to pie_chart_1 function
        per_html2,per_src2 = pie_chart_2(enrollment)
        return render_template('per_studyr1.html',student_name=student_name, per_html1=per_html1, per_html2=per_html2,per_src1=per_src1,per_src2=per_src2 )
    else:
        return 'Enrollment not found in session'
    
@app.route('/per_studyr2/')
def per_studyr2():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        per_html3,per_src3 = pie_chart_3(enrollment)  
        per_html4,per_src4 = pie_chart_4(enrollment)
        return render_template('per_studyr2.html',student_name=student_name, per_html3=per_html3, per_html4=per_html4,per_src3=per_src3,per_src4=per_src4)
    else:
        return 'Enrollment not found in session'

@app.route('/per_studyr3/')
def per_studyr3():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        per_html5,per_src5 = pie_chart_5(enrollment) 
        per_html6,per_src6 = pie_chart_6(enrollment)
        return render_template('per_studyr3.html',student_name=student_name, per_html5=per_html5, per_html6=per_html6,per_src5=per_src5,per_src6=per_src6)
    else:
        return 'Enrollment not found in session'    
    

@app.route('/th_studyr1/')
def th_studyr1():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        th_html1,th_src1 = th_sd_1(enrollment)  
        th_html2,th_src2 = th_sd_2(enrollment) 
        return render_template('th_studyr1.html',student_name=student_name, th_html1=th_html1,th_html2=th_html2,th_src1=th_src1,th_src2=th_src2)
    else:
        return 'Enrollment not found in session'  

@app.route('/th_studyr2/')
def th_studyr2():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        th_html3,th_src3 = th_sd_3(enrollment)  
        th_html4,th_src4 = th_sd_4(enrollment) 
        return render_template('th_studyr2.html',student_name=student_name, th_html3=th_html3,th_html4=th_html4,th_src3=th_src3,th_src4=th_src4)
    else:
        return 'Enrollment not found in session'  

@app.route('/th_studyr3/')
def th_studyr3():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        th_html5,th_src5 = th_sd_5(enrollment)
        th_html6,th_src6 = th_sd_6(enrollment) 
        return render_template('th_studyr3.html',student_name=student_name,th_html5=th_html5, th_html6=th_html6,th_src5=th_src5,th_src6=th_src6)
    else:
        return 'Enrollment not found in session'    

@app.route('/cmp_studyr1/')
def cmp_studyr1():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        cmp_html1,cmp_src2_1,cmp_src3_1 = cmp_1(enrollment)
        cmp_html2,cmp_src2_2,cmp_src3_2 = cmp_2(enrollment) 
        return render_template('cmp_studyr1.html',student_name=student_name,cmp_html1=cmp_html1, cmp_html2=cmp_html2,
                               cmp_src2_1=cmp_src2_1,cmp_src3_1=cmp_src3_1,cmp_src2_2=cmp_src2_2,cmp_src3_2=cmp_src3_2)
    else:
        return 'Enrollment not found in session' 
    
@app.route('/cmp_studyr2/')
def cmp_studyr2():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        cmp_html3,cmp_src2_3,cmp_src3_3 = cmp_3(enrollment)
        cmp_html4,cmp_src2_4,cmp_src3_4 = cmp_4(enrollment) 
        return render_template('cmp_studyr2.html',student_name=student_name,cmp_html3=cmp_html3, cmp_html4=cmp_html4,
                               cmp_src2_3=cmp_src2_3,cmp_src3_3=cmp_src3_3,cmp_src2_4=cmp_src2_4,cmp_src3_4=cmp_src3_4)
    else:
        return 'Enrollment not found in session' 
    
@app.route('/cmp_studyr3/')
def cmp_studyr3():
    enrollment = session.get('enrollment')
    student_name=session.get('student_name')
    if enrollment:
        cmp_html5,cmp_src2_5,cmp_src3_5 = cmp_5(enrollment)
        cmp_html6,cmp_src2_6,cmp_src3_6 = cmp_6(enrollment) 
        return render_template('cmp_studyr3.html',student_name=student_name,cmp_html5=cmp_html5, cmp_html6=cmp_html6,
                               cmp_src2_5=cmp_src2_5,cmp_src3_5=cmp_src3_5,cmp_src2_6=cmp_src2_6,cmp_src3_6=cmp_src3_6)
    else:
        return 'Enrollment not found in session' 
    
if __name__ == '__main__':
    app.run(debug=True)