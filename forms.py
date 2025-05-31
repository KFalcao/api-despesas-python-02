from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        'E‑mail',
        validators=[DataRequired(message="O e‑mail é obrigatório"),
                    Email(message="Formato de e‑mail inválido"),
                    Length(max=150)]
    )
    password = PasswordField(
        'Senha',
        validators=[DataRequired(message="A senha é obrigatória"),
                    Length(min=6, message="Mínimo de 6 caracteres")]
    )
    remember = BooleanField('Lembrar‑me')
    submit = SubmitField('Entrar')


class CadastroForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators=[DataRequired(message="O nome é obrigatório"),
                    Length(max=100, message="Máximo de 100 caracteres")]
    )

    email = StringField(
        'E‑mail',
        validators=[DataRequired(message="O e‑mail é obrigatório"),
                    Email(message="Formato de e‑mail inválido"),
                    Length(max=150)]
    )

    password = PasswordField(
        'Senha',
        validators=[DataRequired(message="A senha é obrigatória"),
                    Length(min=6, message="Mínimo de 6 caracteres")]
    )

    confirm_password = PasswordField(
        'Confirmar Senha',
        validators=[DataRequired(message="Confirmação de senha é obrigatória"),
                    EqualTo('password', message="As senhas devem ser iguais")]
    )

    submit = SubmitField('Cadastrar')
