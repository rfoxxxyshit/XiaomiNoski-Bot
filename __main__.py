print('Starting...')
from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ReplyInlineMarkup, KeyboardButtonRow, KeyboardButtonCallback
import logging
import config

logging.basicConfig(
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	level=logging.WARNING,
	filename='xiaomi.log'
)

bot = TelegramClient('bot', config.API_KEY, config.API_HASH)

@bot.on(events.NewMessage(pattern=r'^/s(t|r|tr)art'))
async def startcmd(event):
	user = await bot(GetFullUserRequest(event.sender_id))
	await event.respond(f'Привет, {user.user.first_name}.\nЯ бот, который поможет тебе поделиться говном в @noski_xiaomi_blyat.\nЯ, кстати, нихуя не умею. Только /add, что бы добавить товар.')

@bot.on(events.NewMessage(pattern='/add'))
async def addcmd(event):
	user = await bot(GetFullUserRequest(event.sender_id))
	async with bot.conversation(user.user.id) as conv:
		await event.respond(f'Отлично! Теперь пришли мне ссылку на товар.\n__Без корявого перевода плез, я не умею это убирать.__')
		response = conv.wait_event(events.NewMessage(incoming=True,from_users=user.user.id))
		response = await response
		link = f"[{response.text}]({response.text})"
		await event.respond('А теперь придумай мне название для этого говна сука.')
		response = conv.wait_event(events.NewMessage(incoming=True,from_users=user.user.id))
		response = await response
		name = response.text
		await event.respond('Заебись! Кто производитель этого говна ебаного?')
		response = conv.wait_event(events.NewMessage(incoming=True,from_users=user.user.id))
		response = await response
		vendor = ('#' + response.text).replace(' ', '_')
		click_button1 = KeyboardButtonCallback("Мобильные телефоны", data=b'telephone')
		click_button2 = KeyboardButtonCallback("Бытовая электроника", data=b'byt_electr')
		click_button3 = KeyboardButtonCallback("Бытовая техника", data=b'byt_tehn')
		click_button4 = KeyboardButtonCallback("Безопасность и защита", data=b'bezopas')
		click_button5 = KeyboardButtonCallback("Компьютер и офис", data=b'computer')
		click_button6 = KeyboardButtonCallback("Багаж и сумки", data=b'bagazh')
		click_button7 = KeyboardButtonCallback("Спорт", data=b'sport')
		click_button8 = KeyboardButtonCallback("Развлечения", data=b'razvle4en')
		click_button9 = KeyboardButtonCallback("Красота и здоровье", data=b'krasota')
		click_button10 = KeyboardButtonCallback("Маски", data=b'maski')
		click_button11 = KeyboardButtonCallback("Одежда", data=b'odezhda')
		click_button12 = KeyboardButtonCallback("Другое", data=b'other')
		line1 = KeyboardButtonRow(buttons=[click_button1, click_button2])
		line2 = KeyboardButtonRow(buttons=[click_button3, click_button4])
		line3 = KeyboardButtonRow(buttons=[click_button5, click_button6])
		line4 = KeyboardButtonRow(buttons=[click_button7, click_button8])
		line5 = KeyboardButtonRow(buttons=[click_button9, click_button10])
		line6 = KeyboardButtonRow(buttons=[click_button11, click_button12])
		btns = ReplyInlineMarkup(rows=[line1, line2, line3, line4, line5, line6])
		await bot.send_message(event.chat.id, 'Ахуенчик! Теперь выбери категорию, в которой находится товар.', buttons=btns)
		response = conv.wait_event(events.CallbackQuery)
		response = await response
		data = response.data.decode('utf-8')
		if data == 'telephone':
			category = '#Мобильные_телефоны'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'byt_electr':
			category = '#Бытовая_электроника'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'byt_tehn':
			category = '#Бытовая_техника'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'bezopas':
			category = '#Безопасность_и_защита'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'computer':
			category = '#Компьютер_и_офис'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'bagazh':
			category = '#Багаж_и_суки'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'sport':
			category = '#Спорт'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'razvle4en':
			category = '#Развлечения'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'krasota':
			category = '#Красота_и_здоровье'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'maski':
			category = '#Маски'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'odezhda':
			category = '#Одежда'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		elif data == 'other':
			category = '#Другое'
			try:
				ppl = user.user.first_name
				await publish(name, vendor, category, link, ppl)
			except Exception:
				await response.answer(message='Fail')
				return await event.respond('Неудачно высрал на канал бля программист хуесос ебливый нахуй')
			await response.answer(message='OK')
			return await event.respond('Удачно высрал на канал ебать.')
		else:
			await event.respond('Ебать ты как из палаты выбрался шизоид ебаный')
			return await response.answer(message='Ты как ебать это сделал нахуй')

async def publish(name, proizv, category, link, ppl):
	# TODO: make link shorteners refuse
	try:
		await bot.send_message(config.CHANNEL, f'{name}\n\nПроизводитель: {proizv}\nКатегория: {category}\n\nСсылка: {link}\nВысрал: {ppl}')
	except Exception:
		raise ValueError

print('Started! Waiting for messages.')
bot.start(bot_token=config.BOT_TOKEN)
bot.run_until_disconnected()