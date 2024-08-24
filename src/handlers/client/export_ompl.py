from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from database import Database

import xml.etree.ElementTree as ET
import logging
import os

router = Router(name=__name__)


def create_opml(feeds: list[dict], output_file: str) -> None:
    opml = ET.Element("opml", version="1.0")

    head = ET.SubElement(opml, "head")
    title = ET.SubElement(head, "title")

    title.text = "RSS Feeds"
    body = ET.SubElement(opml, "body")

    for feed in feeds:
        ET.SubElement(body, "outline", text=feed['title'], type="rss", xmlUrl=feed['rss'])

    tree = ET.ElementTree(opml)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)


@router.callback_query(F.data == 'export_opml')
async def export_opml(callback: CallbackQuery):
    filename = f'{callback.from_user.id}.opml'
    feeds = await Database.get_user_channels(callback.from_user.id)
    create_opml(feeds, filename)

    await callback.message.delete()
    await callback.message.answer_document(document=FSInputFile(path=filename))

    os.remove(filename)

    logging.info(f'User {callback.from_user.id} exported feeds')
