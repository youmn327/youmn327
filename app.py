from flask import Flask, render_template
 
app = Flask(__name__)

# @app.before_request
# def limit_remote_addr():
#     if request.remote_addr == '10.20.30.40':
#         abort(403)  # Forbidden


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/developer')
def developer():
  return render_template('developer.html')
 
# @app.route('/about')
# def about():
#     return 'About 페이지'

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="0.0.0.0",debug = True)
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능