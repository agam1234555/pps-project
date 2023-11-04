from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    address = request.form['address']
    city_state_zip = request.form['city_state_zip']
    phone = request.form['phone']
    email = request.form['email']
    objective = request.form['objective']
    education = request.form['education']
    work_experience = request.form['work_experience']
    volunteer_experience = request.form['volunteer_experience']

    hobbies = request.form['hobbies']
    major = request.form['major']
    university = request.form['university']
    city = request.form['city']
    state = request.form['state']
    course1 = request.form['course1']
    course2 = request.form['course2']
    course3 = request.form['course3']
    course4 = request.form['course4']
    course5 = request.form['course5']
    skill1 = request.form['skill1']
    skill2 = request.form['skill2']
    skill3 = request.form['skill3']
    internship1 = request.form['internship1']
    internship2 = request.form['internship2']
    activity1 = request.form['activity1']
    activity2 = request.form['activity2']
    award1 = request.form['award1']
    award2 = request.form['award2']
    certification1 = request.form['certification1']
    certification2 = request.form['certification2']
    language1 = request.form['language1']
    language2 = request.form['language2']

    return render_template('result.html', 
                           name=name, 
                           address=address, 
                           city_state_zip=city_state_zip, 
                           phone=phone, 
                           email=email, 
                           objective=objective, 
                           education=education, 
                           work_experience=work_experience, 
                           volunteer_experience=volunteer_experience,
                           hobbies=hobbies,
                           major=major,
                           university=university,
                           city=city,
                           state=state,
                           course1=course1,
                           course2=course2,
                           course3=course3,
                           course4=course4,
                           course5=course5,
                           skill1=skill1,
                           skill2=skill2,
                           skill3=skill3,
                           internship1=internship1,
                           internship2=internship2,
                           activity1=activity1,
                           activity2=activity2,
                           award1=award1,
                           award2=award2,
                           certification1=certification1,
                           certification2=certification2,
                           language1=language1,
                           language2=language2
                          )

if __name__ == '__main__':
    app.run(debug=True)
