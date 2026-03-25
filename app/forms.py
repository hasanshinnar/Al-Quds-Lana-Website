from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    EmailField,
    FileField,
    FloatField,
    IntegerField,
    SelectField,
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, NumberRange, length


## login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


## registration Form
class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    FirstName = StringField("First Name", validators=[DataRequired(), length(min=2)])
    LastName = StringField("Last Name", validators=[DataRequired(), length(min=2)])
    password1 = PasswordField(
        "Enter Your Password", validators=[DataRequired(), length(min=6)]
    )
    password2 = PasswordField(
        "Confirm Your Password", validators=[DataRequired(), length(min=6)]
    )
    PhoneNumber = StringField(
        "Phone Number", validators=[DataRequired(), length(min=10, max=15)]
    )
    submit = SubmitField("Sign Up")


## forgot password form
class ForgotPasswordForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Reset Password")


## reset password form
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField(
        "New Password", validators=[DataRequired(), length(min=6)]
    )
    confirm_new_password = PasswordField(
        "Confirm New Password", validators=[DataRequired(), length(min=6)]
    )
    reset_password = SubmitField("Reset Password")


## Change password form
class PasswordChangeForm(FlaskForm):
    current_password = PasswordField(
        "Current Password", validators=[DataRequired(), length(min=6)]
    )
    new_password = PasswordField(
        "New Password", validators=[DataRequired(), length(min=6)]
    )
    confirm_new_password = PasswordField(
        "Confirm New Password", validators=[DataRequired(), length(min=6)]
    )
    change_password = SubmitField("Change Password")


## shop item form
class ShopItemsForm(FlaskForm):
    product_name = StringField("Name of Product", validators=[DataRequired()])
    current_price = FloatField("Current Price", validators=[DataRequired()])
    previous_price = FloatField("Previous Price", validators=[DataRequired()])
    in_stock = IntegerField("In Stock", validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField("Product Picture", validators=[DataRequired()])
    add_product = SubmitField("Add Product")
    promotion_code = StringField("Promotion Code", validators=[length(max=20)])


## order form
class OrderForm(FlaskForm):
    order_status = SelectField(
        "Order Status",
        choices=[
            ("Pending", "Pending"),
            ("Accepted", "Accepted"),
            ("Out for delivery", "Out for delivery"),
            ("Delivered", "Delivered"),
            ("Canceled", "Canceled"),
        ],
    )

    update = SubmitField("Update Status")


## contact us form
class ContactUsForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")
