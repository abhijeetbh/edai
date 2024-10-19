from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
import pandas
import pickle
import warnings


warnings.filterwarnings('ignore')



views=Blueprint('views',__name__)


@views.route('/index', methods=['GET','POST'])
def index():
    ds = pandas.read_csv('web_ready.csv')
    features_to_normalize = ['founded_at', 'funding_total_usd', 'milestones', 'closed_at_year', 'duration_days','log_funding_total_usd']
    min_values = {}
    max_values = {}
    ranges = {}

    for feature in features_to_normalize:
        min_values[feature] = ds[feature].min()
        max_values[feature] = ds[feature].max()
        ranges[feature] = max_values[feature] - min_values[feature]


    if request.method=='POST':
        fa=request.form.get('founded_at')
        tf=request.form.get('funding_total_usd')
        ml=request.form.get('milestones')
        ci=request.form.get('closed_at_year')
        dr=request.form.get('duration_days')
        lf=request.form.get('log_funding_total_usd')
        ca=request.form.get('ca_non_ca')

        fa=pandas.to_numeric(fa)
        tf=pandas.to_numeric(tf)
        ml=pandas.to_numeric(ml)
        ci=pandas.to_numeric(ci)
        dr=pandas.to_numeric(dr)
        lf=pandas.to_numeric(lf)
        ca=pandas.to_numeric(ca)



        fa=(fa-min_values['founded_at'])/ranges['founded_at']
        tf=(tf-min_values['funding_total_usd'])/ranges['funding_total_usd']
        ml=(ml-min_values['milestones'])/ranges['milestones']
        ci=(ci-min_values['closed_at_year'])/ranges['closed_at_year']
        dr=(dr-min_values['duration_days'])/ranges['duration_days']
        lf=(lf-min_values['log_funding_total_usd'])/ranges['log_funding_total_usd']


        user_data_bin=[[fa,tf,ml,ca,ci,dr,lf]]
        user_data_bin=pandas.DataFrame(user_data_bin)

        with open('logistic_model.pkl','rb') as f:
            logistic_model=pickle.load(f)

        with open('random_forest_model.pkl', 'rb') as f:
            random_forest_model=pickle.load(f)

        lrp=logistic_model.predict(user_data_bin)
        lrp=pandas.to_numeric(lrp)

        user_data_mul=[[lrp,fa,tf,ml,ca,ci,dr,lf]]
        user_data_mul=pandas.DataFrame(user_data_mul)
        res=random_forest_model.predict(user_data_mul)

        if res==3:
            flash('Company Status : CLOSED','error')
        if res==2:
            flash('Company Status : ACQUIRED','error')
        if res==1:
            flash('Company Status : IPO','succ')
        if res==4:
            flash('Company Status : OPERATING', 'succ')

    return render_template("index.html")
