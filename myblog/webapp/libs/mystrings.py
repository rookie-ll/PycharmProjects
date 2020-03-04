
# 生成随机字符串
def read_str(shuffix, length=32):
    import string, random
    mystr = string.ascii_letters + string.digits
    # ascii_letters 生成所有字母a-z,A-Z,digits 生成所有数字 0-9
    new_name = ''.join(random.choice(mystr) for i in range(length))
    # 　cgiuce  从某个序列中返回一个随机值
    return new_name + shuffix

def icon():
    form = IconFrom()
    if form.validate_on_submit():
        # 生成随机的文件名字
        shuffix = os.path.splitext(form.icon.data.filename)[1]
        new_str = read_str(shuffix)
        # 保存图片
        photos.save(form.icon.data, name=new_str)
        # 生成缩略图
        filename = os.path.join(current_app.config.get("UPLOADED_PHOTOS_DEST"), new_str)
        img = Image.open(filename)
        img.thumbnail((64, 64))
        # 保存缩略图替换原来的图片
        img.save(filename)
        # 删除原有头像
        if current_user.icon != "default.jpg":
            # 第一次更换的图片不删除，除此之外都删除
            os.remove(os.path.join(current_app.config.get("UPLOADED_PHOTOS_DEST"), current_user.icon))
        # 保存新的头像
        current_user.icon = new_str
        db.session.add(current_user)
        db.session.commit()
        flash("头像已经提交哦", "ok")
        return redirect(url_for("user.icon"))
    return render_template('user/icon.html', form=form)