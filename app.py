from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Для использования flash-сообщений

# Простая модель данных (обычно это будет база данных)
user = {
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "password": "password123"
}


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Обновляем данные пользователя
        user['name'] = name
        user['email'] = email
        user['password'] = password

        flash('Профиль обновлен успешно!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
