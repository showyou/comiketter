#! -*- coding: utf-8 -*-
import logging
import sqlalchemy
from comiketter.lib.base import *

log = logging.getLogger(__name__)

class SearchController(BaseController):

	def index(self):
		# 検索画面を表示

		query = model.Session.query(model.Position)
		order_query = query.order_by(sqlalchemy.sql.desc(model.Position.id))
		c.messages = order_query[:50]
		return render("/index.mako")

	def search(self):
		# 検索結果を返す
		names = request.params.get("name")
		query = model.Session.query(model.Position)
		order_query = query.filter(model.Position.name==names).all()
		c.messages = order_query[:10]
		c.error = names 
		return render("/index.mako")

	def update(self):
		# 更新用フォームを出す
		return render("/update.mako") 

	def updateAction(self):
		# 更新
		name = request.params.get("name")
		pos = request.params.get("position")

		if not name or not pos:
			c.error = u"名前と位置を入力してください"
			return self.update()
        
		try:
			position = model.Position()
			position.name = name
			position.pos = pos

			model.Session.save(position)
			model.Session.commit()
		except Exception, e:
			log.error(e)
			model.Session.rollback()
			c.error = e.message()

		c.error = u"登録できました"	
		return render("/update.mako")

