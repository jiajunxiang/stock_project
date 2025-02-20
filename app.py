import time
import functools
import DBTool
from flask import Flask, render_template, request, redirect, session, url_for


app = Flask(__name__)

app.secret_key='dsfaegdshgf'

def authorization(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        username=session.get('name')
        if not username:
            return redirect(url_for('登录'))
        return func(*args,**kwargs)
    return inner
# ====================   默认跳转  ===========================
@app.route('/',methods=['POST','GET'],endpoint='登录')
def manager_login():
    # 直接访问（get请求），原地跳转
    if request.method == "GET":
        return render_template("login2.html")
        # return render_template("medicine/list.html")
    # 提交表单请求（POST）
    if request.method == "POST":
        # 1.获取请求参数
        name = request.form['name']#获取姓名文本框的输入值
        password=request.form['password']#获取密码框的输入值
        # 2.查询数据库进行比对
        flag=DBTool.login(name,password)
        if flag==1:
            session['name']=name
            return redirect('/index')
        else:
            return render_template("login2.html")

@app.route('/index')
@authorization
def index():
    return render_template("base.html",name=session['name'])

# ====================   一、进货管理模块  ===========================
# 01 入库
@app.route('/addWarehousing')
@authorization
def warehousing():
    return render_template("warehousing/addWarehousing.html", name=session['name'])
@app.route('/add_goods',methods=['POST','GET'])
def addGoods():
    # 直接访问（get请求），原地跳转
    if request.method == "GET":
        return render_template("warehousing/addWarehousing.html")
    # 提交表单请求（POST）
    if request.method == "POST":
        # 获取当前日期
        add_date = time.strftime("%Y-%m-%d", time.localtime())
        # 获取要添加的货物情况
        add_goods = request.form['add_goods']
        add_name = add_goods.split('*')[0]
        add_category = int(add_goods.split('*')[1])
        # 获取要添加的货物数量
        add_number = request.form['add_number']
        #判断数据是否添加成功
        count=DBTool.addWarehousing(add_date,add_name,add_category,add_number)
        if count==1:
            return redirect('/addWarehousing')
        else:
            print('false')
# 02 入库明细初始化
@app.route('/list_warehousing')
@authorization
def warehousingManger():
    result = DBTool.listWarehousing()
    return render_template("warehousing/listWarehousing.html",name=session['name'],warehousing_list=result)
# 03 入库明细修改
@app.route('/edit_warehousing',methods=['POST','GET'])
@authorization
def editWarehousing():
    # 点击修改按钮（获取要修改的原本信息）
    if request.method == 'GET':
        #获取地址栏传递的id
        id = request.args.get('id', type = int)
        #根据id查询数据库相关的信息
        result=DBTool.queryWarehousing(id)
        return render_template("warehousing/editWarehousing.html", name=session['name'], warehousing=result)
    # 修改原本信息（POST表单）
    else:
        id = request.form['id']
        date = request.form['date']
        name = request.form['name']
        category = request.form['category']
        number = request.form['number']
        flag=DBTool.updateWarehousing(id,date,name,category,number)
        if flag==1:
            print('修改成功！')
            return redirect("/list_warehousing")
        else:
            return redirect("/list_warehousing")
# 03 入库明细删除
@app.route('/delete_warehousing')
@authorization
def deleteWarehousing():
    # 获取地址栏传递的id
    id = request.args.get('id', type=int)
    print(id)
    DBTool.deleteWarehousing(id)
    return redirect("/list_warehousing")
# 04 入库明细查询
@app.route('/search_warehousing',methods=['POST','GET'])
@authorization
def searchWarehousing():
    if request.method == 'GET':
        return redirect("/list_warehousing")
    else:
        date = request.form['date']
        result=DBTool.searchWarehousing(date)
        return render_template("warehousing/searchWarehousing.html", name=session['name'], warehousing=result)

# ====================   二、出货管理模块  ===========================
# 01 出库
@app.route('/delOutbound')
@authorization
def outbound():
    return render_template("outbound/delOutbound.html", name=session['name'])
@app.route('/del_goods',methods=['POST','GET'])
def delGoods():
    # 直接访问（get请求），原地跳转
    if request.method == "GET":
        return render_template("outbound/delOutbound.html")
    # 提交表单请求（POST）
    if request.method == "POST":
        # 获取当前日期
        add_date = time.strftime("%Y-%m-%d", time.localtime())
        # 获取要添加的货物情况
        del_goods = request.form['del_goods']
        del_name = del_goods.split('*')[0]
        del_category = int(del_goods.split('*')[1])
        # 获取要添加的货物数量
        del_number = request.form['del_number']
        #判断数据是否添加成功
        count=DBTool.delOutbound(add_date,del_name,del_category,del_number)
        if count==1:
            return redirect('/delOutbound')
        else:
            print('false')
# 02 出库明细初始化
@app.route('/list_outbound')
@authorization
def outboundManger():
    result = DBTool.listOutbound()
    return render_template("outbound/listOutbound.html",name=session['name'],outbound_list=result)
# 03 出库明细修改
@app.route('/edit_outbound',methods=['POST','GET'])
@authorization
def editOutbound():
    # 点击修改按钮（获取要修改的原本信息）
    if request.method == 'GET':
        #获取地址栏传递的id
        id = request.args.get('id', type = int)
        #根据id查询数据库相关的信息
        result=DBTool.queryOutbound(id)
        return render_template("outbound/editOutbound.html", name=session['name'], outbound=result)
    # 修改原本信息（POST表单）
    else:
        id = request.form['id']
        date = request.form['date']
        name = request.form['name']
        category = request.form['category']
        number = request.form['number']
        flag=DBTool.updateOutbound(id,date,name,category,number)
        if flag==1:
            print('修改成功！')
            return redirect("/list_outbound")
        else:
            return redirect("/list_outbound")
# 03 出库明细删除
@app.route('/delete_outbound')
@authorization
def deleteOutbound():
    # 获取地址栏传递的id
    id = request.args.get('id', type=int)
    DBTool.deleteOutbound(id)
    return redirect("/list_outbound")
# 04 出库明细查询
@app.route('/search_outbound',methods=['POST','GET'])
@authorization
def searchOutbound():
    if request.method == 'GET':
        return redirect("/list_outbound")
    else:
        date = request.form['date']
        result=DBTool.searchOutbound(date)
        return render_template("outbound/searchOutbound.html", name=session['name'], outbound=result)

# ====================   三、库存管理模块  ===========================
# 01 新增
@app.route('/addStock')
@authorization
def stock():
    return render_template("stock/addStock.html", name=session['name'])
@app.route('/add_stock',methods=['POST','GET'])
def addStock():
    # 直接访问（get请求），原地跳转
    if request.method == "GET":
        return render_template("stock/addStock.html")
    # 提交表单请求（POST）
    if request.method == "POST":
        # 获取要添加的货物情况
        new_name = request.form['new_name']
        # 获取要添加的货物数量
        new_number = request.form['new_number']
        if new_number=='':
            new_number=0
        #判断数据是否添加成功
        count=DBTool.addStock(new_name,new_number)
        if count==1:
            return redirect('/addStock')
        else:
            print('false')
# 02 初始化
@app.route('/list_stock')
@authorization
def stockManger():
    result = DBTool.listStock()
    return render_template("stock/listStock.html",name=session['name'],stock_list=result)
# 03 修改
@app.route('/edit_stock',methods=['POST','GET'])
@authorization
def editStock():
    # 点击修改按钮（获取要修改的原本信息）
    if request.method == 'GET':
        #获取地址栏传递的参数
        name = request.args.get('name', type = str)
        print(name)
        #根据id查询数据库相关的信息
        result=DBTool.queryStock(name)
        return render_template("stock/editStock.html", name=session['name'], stock=result)
    # 修改原本信息（POST表单）
    else:
        name = request.form['name']
        number = request.form['number']
        flag=DBTool.updateStock(name,number)
        if flag==1:
            print('修改成功！')
            return redirect("/list_stock")
        else:
            return redirect("/list_stock")
# 03 删除
@app.route('/delete_stock')
@authorization
def deleteStock():
    # 获取地址栏传递的id
    name = request.args.get('name', type=str)
    DBTool.deleteStock(name)
    return redirect("/list_stock")
# 04 查询
@app.route('/search_stock',methods=['POST','GET'])
@authorization
def searchStock():
    if request.method == 'GET':
        return redirect("/list_stock")
    else:
        name = request.form['name']
        result=DBTool.searchStock(name)
        return render_template("stock/searchStock.html", name=session['name'], stock=result)

# ====================   药品管理模块  ===========================
# 01 初始化
@app.route('/list')
@authorization
def list():
    result = DBTool.list()
    return render_template("medicine/list.html",name=session['name'],stock_list=result)
# 03 修改
@app.route('/edit',methods=['POST','GET'])
@authorization
def edit():
    # 点击修改按钮（获取要修改的原本信息）
    if request.method == 'GET':
        #获取地址栏传递的参数
        id = request.args.get('id', type = str)
        #根据id查询数据库相关的信息
        result=DBTool.search(id)
        return render_template("medicine/edit.html", name=session['name'], stock=result)
    # 修改原本信息（POST表单）
    else:
        name=request.form['name']
        average_cost = request.form['average_cost']
        cost = request.form['cost']
        other=request.form['other']
        flag=DBTool.update(name,average_cost,cost,other)
        if flag==1:
            print('修改成功！')
            return redirect("/list")
        else:
            return redirect("/list")
# 03 删除
@app.route('/delete')
@authorization
def delete():
    # 获取地址栏传递的id
    id = request.args.get('id', type=str)
    DBTool.delete(id)
    return redirect("/list")
# 04 查询
@app.route('/search',methods=['POST','GET'])
@authorization
def search():
    if request.method == 'GET':
        return redirect("/list")
    else:
        id = request.form['id']
        result=DBTool.search(id)
        return render_template("medicine/search.html", name=session['name'], stock=result)








# ==================================其他功能===========================
# 退出系统
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('登录'))

if __name__ == '__main__':
    app.run(debug=True)


