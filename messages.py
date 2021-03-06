#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings
start = {'mes':'start',
    'text':'''
Данный бот нацелен на поиск заинтересованной аудитории для вашего канала, каторая будет просматривать ваши посты, это не накрутка подписчиков, это обзор вашего канала в течении суток. Исполнитлям разрешено отписаться от вашего канала, если он им не интерсен, через 24 часа после вступления в ваш канал.
Поэтому в нашем боте самые низкие цены.
Приглашайте друзей и получайте 80% от их заработка, обеспечьте себе пассивный доход!
    
    ''',
    'markup':[
    [
        '➕ Подписаться на канал за 💰'
    ],
    [
        '🤠 Рекламировать свой канал 💣'
    ],
       [
        '🏠 Личный кабинет','💰 Hyip ExpertBot','🏦 Банк'
    ],
    [
        'О боте 🦋','🔥 Чат 💬','📢 ПИАР'
    ],
    [
        '⭐️ Оценить бота ⭐️','Рефералы тут ⚠'
     ],   
    
]}
# '💵 Баланс','👥 Рефералы'
admin = {
    'text':'Приветсвую вас в админке бота',
    'markup':[
        ['заявки на вывод','📊 Статистика'],['сделать рассылку'],['изменить баланс','пополнить баланс'],['⛔️ Отмена']
    ]
}

for_advert={
    'text':'''*⚠️ИНСТРУКЦИЯ⚠️ *
```
🔀Чтобы начать продвижение Вашего канала, необходимо:

1. Добавить этого бота в администраторы Вашего канала.

2. Переслать любой пост из Вашего канала в чат с ботом.

3. Проследовать дальнейшим указаниям бота

```[ ]({})'''.format(settings.tutorial_url),
    'markup':[['Мои заказы'],['⛔️ Отмена']],
    'success':{
        'text':'''👑 Все сделано правильно!
👥Теперь введите стоимость 1 подписчика на ваш канал в рублях
⛔️Минимальная стоимость: {} рублей.'''.format(settings.min_post_cost),
        'markup':[['⛔️ Отмена']]
    },
    'success_count':{
        'text': '''Теперь введите желаемое количество подписчиков''',
        'markup': [['⛔️ Отмена']]
    },
    'success_apply': {
        'text': '''Стоимость продвижения канала: {} * {} = {}
        Все верно? Подтвердить?''',
        'markup': [['✅ Подтвердить'], ['⛔️ Отмена']]
    },
    'error_not_admin': {
        'text': '''🚫 Ошибка! Бот не обнаружен в администраторах канала. Добавьте бота и нажите кнопку ниже.''',
        'markup': [[{'text':'Проверить','data':'check_admin'},{'text':'❌ Отклонить','data':'cancel_check_admin'}]]
    },
    'error_low_cost': {
        'text': '''🚫 Ошибка!
Минимальная стоимость одного подписчика -  {} руб'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_done':{
        'text': '''Канал добавлен!''',
        'markup': start['markup']
    },
    'error_money':{
        'text': '''🚫 Ошибка! Недостаточно средст на счету''',
        'markup': start['markup']
    },
    'already_in':{
        'text': '''🚫 Ошибка! Канал можно будет добавить заново после вступления добавленного количества подписчиков''',
        'markup': [['Мои заказы'],['⛔️ Отмена']]
    }
}


view_end = {
    'text':'''🎉Держи монетку, вы получили: {} рублей.
💲Ваш баланс: {} рублей''',
    'markup':start['markup']
}

sub_err= {
    'text':'⛔️Каналы закончились, но если ваш реферал тоже подпишется на эти каналы, вы получите 80% от его зароботка, количество рефералов не ограничено. Приглашайте друзей по вашей реферальной ссылке (ссылка находится в вашм личном кабинете бота), обеспечте себе пассивный доход! 💰',
    'markup':start['markup']
}



stat={
    'text':'''🔀 *Статистика проекта*:
    😎Участников проекта: %all_users%
    🤠Новые участники: %users_today%
    🚀Каналов на продвижении: %posts_count%
    💰Заработано всего: %money_for_views%
    🎁Выплачено всего: %money_out%''',
    'markup':start['markup']
}



chatix={
    'text':'''https://t.me/joinchat/JLzJPkgO-xxYxoKbZ2Iltg''',
    'markup':start['markup']
}


decline={
    'text':'''Операция отменена''',
    'markup':start['markup']
}



out_pay = {
    'text':'''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(settings.min_out_pay),
    'markup':[['⛔️ Отмена']],
    'ya':{
        'text': '''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(
            settings.min_out_pay),
        'markup': [['⛔️ Отмена']],
    },
    'error_min_pay': {
        'text': 'Ошибка! Нельзя вывести меньше минимальной суммы',
        'markup': [['⛔️ Отмена']]
    },
    'error_max_pay': {
        'text': 'Ошибка! У вас недостаточно средств на счету',
        'markup': [['⛔️ Отмена']]
    },
    'enter_ya': {
        'text': 'Хорошо! Теперь введите номер вашего кошелька',
        'markup': [['⛔️ Отмена']]
    },
    'enter_qiwi': {
        'text': 'Хорошо! Теперь введите номер телефона, который привязан к QIWI',
        'markup': [['Отправить номер вашего телефона'],['⛔️ Отмена']]
    },
    'success': {
        'text': 'Ваша заявка одобрена, выплаты производятся в ручном режиме, так что придётся немного подождать!!',
        'markup': start['markup']
    }
}

balance={
    'code':{
        'text':'''🔥Для автоматического пополнения баланса переведите нужную сумму на этот QIWI кошелек {} со следующим кодом в комментарии к переводу.
⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!

⚡️После перевода сумма зачислится в течение 1 минуты'''.format(settings.number),
        'markup':start['markup']
    },
    'success':{
        'text': 'Ваш счет пополнен на {}',
        'markup': start['markup']
    },
    'ya':{
        'text': '''🔥 Для автоматического пополнения баланса переведите нужную сумму по [ссылке](https://money.yandex.ru/to/{}) со следующим кодом в комментарии к переводу.
⛔️ОЧЕНЬ ВАЖНО оставить код в комментарии и не чего более, иначе платеж не будет засчитан!

⚡️После перевода сумма зачислится в течение 1 минуты'''.format(settings.ya_number),
        'markup': start['markup']
    }

}


edit_balance={
    'text': 'Введи имя пользователя с @username или его id',
    'markup':[['⛔️ Отмена']],
    'err_user':{
        'text':'Ошибка, пользователь не найден',
        'markup':[['⛔️ Отмена']]
    },
    'enter_balance':{
        'text': 'Введите новый баланс пользователя, сейчас он %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success':{
        'text': 'Новый баланс установлен!',
        'markup': admin['markup']
    },
    'err_number':{
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }

}

pay_balance={
    'text': 'Введи имя пользователя с @username или его id',
    'markup':[['⛔️ Отмена']],
    'err_user':{
        'text':'Ошибка, пользователь не найден',
        'markup':[['⛔️ Отмена']]
    },
    'enter_balance':{
        'text': 'Введите на сколько пополнить, сейчас баланс %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success':{
        'text': 'Баланс пополнен!',
        'markup': admin['markup']
    },
    'err_number':{
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }

}

mailer = {
    'text':'Отправь нужное сообщение для рассылки',
    'markup':[['⛔️ Отмена']],
    'confirm':{
        'text': 'Принято! Разослать?',
        'markup': [['⛔️ Отмена'],['✅ Подтвердить']],
    },
    'success':{
        'text': 'Ок!',
        'markup': admin['markup']
    }
}
