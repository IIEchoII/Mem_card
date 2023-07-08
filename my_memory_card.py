from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q = Question("Выбери перевод слова ""переменная","variable","variation","varity","input")
questions_list = []
questions_list.append(Question("Государственный язык португалии","Португальский","Английский","Испанский","Французский"))
questions_list.append(Question("Какого цвета нет на флаге Росси?","Зелёный","Красный","Синий","Белый"))
questions_list.append(Question("Название самого высокого водопада","Анхель","Тугела","Олоупена","Браун"))
questions_list.append(Question("Кто из них биолог?","Антони ван Левенгук","Александр Сергеевич Пушкин","Иван Фёдорович Крузенштерн","Пётр Чайковский"))
questions_list.append(Question("Как называется язык программирования на котором написана эта программа?","Python","Java","C++","C#"))
questions_list.append(Question("Сколько дней в високосном году?","366","365","364","363"))
questions_list.append(Question("В каком году закончилась Ⅰ мировая война?","1918","1914","1945","1941"))
questions_list.append(Question("Столица Португалии?","Лиссабон","Нью-Йорк","Мадрид","Хельсинки"))
questions_list.append(Question("В каком году был создан первый язык программирования?","1949","1967","1982","1924"))
questions_list.append(Question("Какой страны не существует?","Караганда","Тувалу","Кирибати","Коморы"))

lb_Question = QLabel("Самый сложный вопрос в мире!")
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("Правильно/Неправильно")
lb_Correct = QLabel("Правильный ответ")
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(400,200)
btn_OK = QPushButton("Ответить")
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn1 = QRadioButton("Энцы")
rbtn2= QRadioButton("Чулымцы")
rbtn3= QRadioButton("Смурфы")
rbtn4= QRadioButton("Алеуты")

layout_card = QVBoxLayout()
layout_card.setSpacing(5)
layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()
layoutline1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutline2.addWidget(RadioGroupBox)
layoutline3.addStretch(1)
layoutline3.addWidget(btn_OK,stretch=2)
layoutline3.addStretch(1)
layout_card.addLayout(layoutline1)
layout_card.addLayout(layoutline2)
layout_card.addLayout(layoutline3)
main_win.setLayout(layout_card)

layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans1.addWidget(rbtn1)
layout_ans1.addWidget(rbtn3)
layout_ans2.addWidget(rbtn2)
layout_ans2.addWidget(rbtn4)
layout_ans3.addLayout(layout_ans1)
layout_ans3.addLayout(layout_ans2)
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
RadioGroupBox.setLayout(layout_ans3)


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2 )
AnsGroupBox.setLayout(layout_res)
layoutline2.addWidget(AnsGroupBox)
layoutline1.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    global a
    if a == True:
        show_result()
    elif a == False:
        show_question()

answers = [rbtn1,rbtn2,rbtn3,rbtn4]

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
        print("Статисктика\n-Всего вопросов:",main_win.total,"\n-Правильных ответов:",main_win.score)
        print("Рейтинг:",(main_win.score / main_win.total * 100),"%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно!")
            print("Рейтинг:", (main_win.score / main_win.total * 100),"%")

def next_question():   
    main_win.total += 1
    print("Статисктика\n-Всего вопросов:",main_win.total,"\n-Правильных ответов:",main_win.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()
main_win.score = 0
main_win.total = 0
next_question()
btn_OK.clicked.connect(click_OK)
main_win.show()
app.exec_()
