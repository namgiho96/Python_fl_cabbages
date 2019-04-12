from flask import Flask, jsonify, render_template, request
import re
import tensorflow as tf
import  numpy as np
#import datatime
from pandas.io.parsers import  read_csv
from db import Database
app = Flask(__name__)

"""
model = tf.global_variables_initializer()
data = read_csv('price_data.csv', sep=',')
xy = np.array(data, dtype=np.float32)

x_data = xy[:, 1:-1]
y_data = xy[:, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name='weight')
b = tf.placeholder(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) +b

cost = tf.reduce_mean(tf.square(hypothesis -Y))

optimizer = tf.train.ProximalGradientDescentOptimizer(learning_rate=0.000005)

train = optimizer.minimize(cost)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(100001):
    cost_, hypo_, _ = sess.run([cost, hypothesis, train]
                               , feed_dict={X:x_data, Y:y_data})
    if step % 500 == 0:
        print("#", step, "손실 비용:", cost_)
        print("- 배추 가격 :", hypo_[0])

saver = tf.train.Saver()
save_path = saver.save(sess, "./data/saved.cpkt")
print("학습된 모델을 저장합니다")
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return jsonify()


@app.route('/login', methods=['POST'])
def login():
    print("------------로그인 들어옴--------------------")
    db = Database()
    #db.create()
    #db.insert()
    userid = request.form['userid']
    password = request.form['password']
    print('아이디 {}, 비번 {}'.format(userid,password))
    row = db.login(userid, password)
    print(' 회원 정보 {}'.format(row))

    return render_template("main.html")

@app.route('/logout')
def logout():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
