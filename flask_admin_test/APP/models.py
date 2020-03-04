from APP.extends import db

s_t = db.Table(
    's_t',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'),primary_key=True),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'),primary_key=True)
)

t_c = db.Table(
    't_c',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'),primary_key=True),
    db.Column('class17_id', db.Integer, db.ForeignKey('class17.id'),primary_key=True)
)


class Class17(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    class_num = db.Column(db.Integer, unique=True)
    student_id = db.relationship('Student', backref='class17.id', lazy='dynamic')
    #teacher_id=db.relationship('Teacher',backref='class17.id')
    #teachers = db.relationship('Teacher', secondary=t_c, backref=db.backref('class17s', lazy='dynamic', cascade='all'))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    class_id = db.Column(db.Integer, db.ForeignKey('class17.id'))
    teachers = db.relationship('Teacher', secondary=s_t, backref=db.backref('students', lazy='dynamic'))


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    #class_id = db.Column(db.Integer, db.ForeignKey('class17.id'))
    class17s = db.relationship('Class17', secondary=t_c, backref=db.backref('teachers', lazy='dynamic'))
