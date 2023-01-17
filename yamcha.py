import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from yamchamodels import callAPI
from flask_mail import Mail,Message
from email.mime.text import MIMEText
import smtplib

UPLOAD_FOLDER = './static/gazou/post'
# アップロードを許可する拡張子の設定
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)


# flashメッセージ用に任意のキーを設定
app.secret_key = 'flash_key'
'''
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="swissmadecarandache@gmail.com"
app.config['MAIL_PASSWORD']='qomfyfingpbcdebk'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
'''
mail=Mail(app)


# アップロードされたファイルの拡張子チェック
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# rootディレクトリにアクセスした場合の挙動
@app.route('/bukuuzyutu', methods=['GET', 'POST'])
def bukuuzyutu():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルを選択してね')
            return render_template('bukuuzyutu.html')

        file = request.files['file']
        if not allowed_file(file.filename):
            flash('拡張子はpng, jpg, jpegのみ使用可能!')
            return render_template('bukuuzyutu.html')
        else:
            filename  = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            return render_template('soukidan.html', file_path=file_path)
    else:
        return render_template('bukuuzyutu.html')

# 推論ボタン押下時の挙動
@app.route('/bukuuzyutu/rougawhowhoken', methods=['GET', 'POST'])
def rougawhowhoken():
    if request.method == 'POST':
        file_path = request.form['image']
        data = callAPI(file_path)

        return render_template(
            		'rougawhowhoken.html', 
					yamcha_data=data,
					file_path=file_path
				)
    else:
        return render_template('bukuuzyutu.html')

# rootディレクトリにアクセスした場合の挙動
@app.route('/', methods=['GET', 'POST'])
def index():
    
            return render_template('index.html')

 # rootディレクトリにアクセスした場合の挙動
@app.route('/haikei', methods=['GET', 'POST'])
def haikei():
    
            return render_template('haikei.html')

# rootディレクトリにアクセスした場合の挙動
@app.route('/zukan', methods=['GET', 'POST'])
def zukan():
    
            return render_template('zukan.html')

# rootディレクトリにアクセスした場合の挙動
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
            return render_template('contact.html')

@app.route('/contact/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method=="POST":
       # email= request.form['email']
        #subject=request.form['subject']
        #msg=request.form['message']
        ''' how=request.form.get('how')
        bodytext=how
        msg=MIMEText(bodytext)
        msg['how']=how'''
        from_email = 'swissmadecarandache@gmail.com'
        to_email = 'swissmadecarandache@gmail.com'
        account = 'swissmadecarandache@gmail.com'
        password = 'qomfyfingpbcdebk'
        subject='評価用アンケート'
        seibetu=request.form.get('seibetu')
        nenndai = request.form.get('nenndai')
        about = request.form.get('about')
        bodytext = "性別：" + seibetu + "\n" +"年代：" + nenndai + "\n" + "自由記載：" + about
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(account, password)
        msg = MIMEText(bodytext)
        msg['subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server.send_message(msg)
        server.close()
        return render_template("result.html",success=True)

'''   message=Message("評価用アンケート",sender="swissmadecarandache@gmail.com",recipients=["swissmadecarandache@gmail.com"])
        message.body=msg
        mail.send(message)
        success="Message sent"
                return render_template("result.html",success=success)

'''
'''
@app.route('/contact/send_message', methods=['GET', 'POST'])
def send_message():
        return render_template("result.html")
'''

@app.route('/bukuuzyutu/americankaru', methods=['GET', 'POST'])
def americankaru_img():
#    if request.method == 'POST'
    return render_template('zukan.html')

@app.route('/bukuuzyutu/americankokka', methods=['GET', 'POST'])
def americankokka_img():
#    if request.method == 'POST':
    return 'b'

@app.route('/bukuuzyutu/americansyoto', methods=['GET', 'POST'])
def americansyoto_img():
#    if request.method == 'POST':
    return 'c'

@app.route('/bukuuzyutu/italian', methods=['GET', 'POST'])
def italian_img():
#    if request.method == 'POST':
    return 'd'

@app.route('/bukuuzyutu/uxerusyu', methods=['GET', 'POST'])
def uxerusyu_img():
#    if request.method == 'POST':
    return 'e'

@app.route('/bukuuzyutu/ekizo', methods=['GET', 'POST'])
def ekizo_img():
#    if request.method == 'POST':
    return 'f'

@app.route('/bukuuzyutu/kanin', methods=['GET', 'POST'])
def kanin_img():
#    if request.method == 'POST':
    return 'g'

@app.route('/bukuuzyutu/kizi', methods=['GET', 'POST'])
def kizi_img():
#    if request.method == 'POST':
    return 'h'

@app.route('/bukuuzyutu/kyabaria', methods=['GET', 'POST'])
def kyabaria_img():
#    if request.method == 'POST':
    return 'i'

@app.route('/bukuuzyutu/golden', methods=['GET', 'POST'])
def golden_img():
#    if request.method == 'POST':
    return 'j'

@app.route('/bukuuzyutu/saiberian', methods=['GET', 'POST'])
def saiberian_img():
#    if request.method == 'POST':
    return 'k'

@app.route('/bukuuzyutu/sabatora', methods=['GET', 'POST'])
def sabatora_img():
#    if request.method == 'POST':
    return 'l'

@app.route('/bukuuzyutu/sabineko', methods=['GET', 'POST'])
def sabineko_img():
#    if request.method == 'POST':
    return 'm'

@app.route('/bukuuzyutu/sizu', methods=['GET', 'POST'])
def sizu_img():
#    if request.method == 'POST':
    return 'n'

@app.route('/bukuuzyutu/syetto', methods=['GET', 'POST'])
def syetto_img():
#    if request.method == 'POST':
    return 'o'

@app.route('/bukuuzyutu/siberian', methods=['GET', 'POST'])
def siberian_img():
#    if request.method == 'POST':
    return 'p'

@app.route('/bukuuzyutu/jack', methods=['GET', 'POST'])
def jack_img():
#    if request.method == 'POST':
    return 'q'

@app.route('/bukuuzyutu/sukote', methods=['GET', 'POST'])
def sukote_img():
#    if request.method == 'POST':
    return 'r'

@app.route('/bukuuzyutu/somari', methods=['GET', 'POST'])
def somari_img():
#    if request.method == 'POST':
    return 's'

@app.route('/bukuuzyutu/tiwawa', methods=['GET', 'POST'])
def tiwawa_img():
#    if request.method == 'POST':
    return 't'

@app.route('/bukuuzyutu/toypu', methods=['GET', 'POST'])
def toypu_img():
#    if request.method == 'POST':
    return 'u'

@app.route('/bukuuzyutu/noruxe', methods=['GET', 'POST'])
def noruxe_img():
#    if request.method == 'POST':
    return 'v'

@app.route('/bukuuzyutu/pagu', methods=['GET', 'POST'])
def pagu_img():
#    if request.method == 'POST':
    return 'w'

@app.route('/bukuuzyutu/papiyon', methods=['GET', 'POST'])
def papiyon_img():
#    if request.method == 'POST':
    return 'x'

@app.route('/bukuuzyutu/biguru', methods=['GET', 'POST'])
def biguru_img():
#    if request.method == 'POST':
    return 'y'

@app.route('/bukuuzyutu/bizyon', methods=['GET', 'POST'])
def bizyon_img():
#    if request.method == 'POST':
    return 'z'

@app.route('/bukuuzyutu/puritexi', methods=['GET', 'POST'])
def puritexi_img():
#    if request.method == 'POST':
    return 'aa'

@app.route('/bukuuzyutu/hurenti', methods=['GET', 'POST'])
def hurenti_img():
#    if request.method == 'POST':
    return 'ab'
    
@app.route('/bukuuzyutu/pekini', methods=['GET', 'POST'])
def pekini_img():
#    if request.method == 'POST':
    return 'ac'

@app.route('/bukuuzyutu/perusya', methods=['GET', 'POST'])
def perusya_img():
#    if request.method == 'POST':
    return 'ad'

@app.route('/bukuuzyutu/bengaru', methods=['GET', 'POST'])
def bengaru_img():
#    if request.method == 'POST':
    return 'ae'

@app.route('/bukuuzyutu/bodakori', methods=['GET', 'POST'])
def bodakori_img():
#    if request.method == 'POST':
    return 'af'

@app.route('/bukuuzyutu/pome', methods=['GET', 'POST'])
def pome_img():
#    if request.method == 'POST':
    return render_template('pome.html')

@app.route('/bukuuzyutu/maruti', methods=['GET', 'POST'])
def maruti_img():
#    if request.method == 'POST':
    return 'ah'

@app.route('/bukuuzyutu/manti', methods=['GET', 'POST'])
def manti_img():
#    if request.method == 'POST':
    return 'ai'

@app.route('/bukuuzyutu/minisyu', methods=['GET', 'POST'])
def minisyu_img():
#    if request.method == 'POST':
    return 'aj'

@app.route('/bukuuzyutu/minidakku', methods=['GET', 'POST'])
def minidakku_img():
#    if request.method == 'POST':
    return 'ak'

@app.route('/bukuuzyutu/minipin', methods=['GET', 'POST'])
def minipin_img():
#    if request.method == 'POST':
    return 'al'

@app.route('/bukuuzyutu/minuetto', methods=['GET', 'POST'])
def minuetto_img():
#    if request.method == 'POST':
    return 'am'

@app.route('/bukuuzyutu/meinkun', methods=['GET', 'POST'])
def meinkun_img():
#    if request.method == 'POST':
    return 'an'

@app.route('/bukuuzyutu/yokusya', methods=['GET', 'POST'])
def yokusya_img():
#    if request.method == 'POST':
    return 'ao'

@app.route('/bukuuzyutu/ragama', methods=['GET', 'POST'])
def ragama_img():
#    if request.method == 'POST':
    return 'ap'

@app.route('/bukuuzyutu/ragudoru', methods=['GET', 'POST'])
def ragudoru_img():
#    if request.method == 'POST':
    return 'aq'

@app.route('/bukuuzyutu/raburadoru', methods=['GET', 'POST'])
def raburadoru_img():
#    if request.method == 'POST':
    return 'ar'

@app.route('/bukuuzyutu/rosian', methods=['GET', 'POST'])
def rosian_img():
#    if request.method == 'POST':
    return 'as'

@app.route('/bukuuzyutu/kuroneko', methods=['GET', 'POST'])
def kuroneko_img():
#    if request.method == 'POST':
    return 'at'

@app.route('/bukuuzyutu/mikeneko', methods=['GET', 'POST'])
def mikeneko_img():
#    if request.method == 'POST':
    return 'au'

@app.route('/bukuuzyutu/sibainu', methods=['GET', 'POST'])
def sibainu_img():
#    if request.method == 'POST':
    return 'av'

@app.route('/bukuuzyutu/akitaken', methods=['GET', 'POST'])
def akitaken_img():
#    if request.method == 'POST':
    return 'aw'

@app.route('/bukuuzyutu/tyatora', methods=['GET', 'POST'])
def tyatora_img():
#    if request.method == 'POST':
    return 'ax'




# メインで実行される関数
if __name__ == '__main__':
     #   app.run(debug=True)
    app.run(host='127.0.0.1', port=8000, debug=True)