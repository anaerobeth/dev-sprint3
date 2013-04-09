import flask, flask.views
import utils

class Reverse(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('reverse.html')

    @utils.login_required
    def post(self):
        s = str(flask.request.form['expression'])
        #reverse the string!
        r = ""
        for i in s:
            r = i + r
        flask.flash(r)
        return flask.redirect(flask.url_for('reverse'))
