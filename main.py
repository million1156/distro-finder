from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option, SlashCommandChoice, Embed
import requests
from datetime import datetime, timedelta
import asyncio
from bs4 import BeautifulSoup
import re
import random
import websockets
import json

bot = Client(intents=Intents.ALL)

@slash_command(name="upccheck", description="Checks which company a UPC was created by")
@slash_option(name="upc", description="UPC to use", required=True, opt_type=OptionType.STRING)
async def scrapelink(ctx: SlashContext, upc: str):
    await ctx.defer()
    testLink = f"https://www.gs1.org/services/verified-by-gs1/results?gtin={upc}&ajax_form=1&_wrapper_format=html&_wrapper_format=drupal_ajax"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Mode": "cors",
        "Host": "www.gs1.org",
        "Origin": "https://www.gs1.org",
        "Content-Length": "1444",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Referer": f"https://www.gs1.org/services/verified-by-gs1/results?gtin={upc}",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Cookie": "_ce.s=v~c7bdf45ad2bce8d0fdaf1093e5445a91f3b947f0~lcw~1708643514072~lva~1708643379304~vpv~0~v11.fhb~1708643379769~v11.lhb~1708643501360~v11.cs~77096~v11.s~747f2ed0-d1d7-11ee-923f-f76cae8c0d53~v11.sla~1708643514170~lcw~1708643514170; _ce.clock_data=-87%2C75.35.141.64%2C1%2C8f6b51a36078c08d3ccd4deefba00e15; _ce.clock_event=1; _ce.irv=new; cebs=1; cebsp_=1; _ga=GA1.1.211149362.1708643378; _ga_49BMZJWL9R=GS1.1.1708643378.1.0.1708643378.60.0.0; Drupal.visitor.teamMember=no; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+22+2024+17%3A09%3A34+GMT-0600+(Central+Standard+Time)&version=6.30.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=US%3BTX&AwaitingReconsent=false; SSESS924798324822d30ca03a54f5de4e433f=RfUFDnodabv21L0ChYrDdl0KkSPObRtMDKS5o%2C4Y5S4rln45; vfs_token=7RGv329hHAf2-iKrxIbl0NWsyNvTOpihVanqb-crGpU; gsone_verified_search_terms_1_2=1; OptanonAlertBoxClosed=2024-02-22T22:53:21.663Z",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "search_type": "gtin",
        "gtin": upc,
        "gln": "",
        "country": "",
        "street_address": "",
        "postal_code": "",
        "city": "",
        "company_name": "",
        "other_key_type": "",
        "other_key": "",
        "vfs_token": "7RGv329hHAf2-iKrxIbl0NWsyNvTOpihVanqb-crGpU",
        "captcha_sid": "2627596",
        "captcha_token": "RECAPTCHA_TOKEN",
        "form_build_id": "form-W274pwIIm6tOi02zJN7jFlgpVKDO4PTSB6u0SJnLQeQ",
        "form_id": "verified_search_form",
        "_triggering_element_name": "gtin_submit",
        "_triggering_element_value": "Search",
        "_drupal_ajax": "1",
        "ajax_page_state[theme]": "gsone_revamp",
        "ajax_page_state[theme_token]": "",
        "ajax_page_state[libraries]": "addtoany/addtoany,back_to_top/back_to_top_icon,back_to_top/back_to_top_js,bootstrap_barrio/bootstrap-icons,bootstrap_barrio/global-styling,bootstrap_barrio/messages_white,bootstrap_barrio/node,bootstrap_styles/plugin.background_color.build,bootstrap_styles/plugin.margin.build,bootstrap_styles/plugin.padding.build,bootstrap_styles/plugin.scroll_effects.build,captcha/base,ckeditor_bootstrap_tabs/tabs,core/drupal.states,core/internal.jquery.form,core/jquery.form,fontawesome/fontawesome.svg,fontawesome/fontawesome.svg.shim,gsone_revamp/bootstrap_cdn,gsone_revamp/global-styling,gsone_revamp/select,gsone_revamp/select-library,gsone_verified_search/rateit,gsone_verified_search/verified_search,recaptcha_once/recaptcha_once,system/base,views/views.module,webform/libraries.jquery.intl-tel-input"
    }
    response = requests.post(testLink, headers=headers, data=data)

    try:
     res = json.loads(response.content)
     print(res)
     company = res[4]["settings"]["gsone_verified_search"]["statusMessage"]
     company = company.replace("Currently, no product information has been provided for this product.", "")
     company = company.replace("This number is registered to company: ", "")
    except:
        return "Error"
    if company == "Error":
        embed = Embed(
            title="Error",
            description=f"<:error:1208885864424407141> There was an error scraping the link. Please try again later :(",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        return
    embed = Embed(
        title="Success!",
        description=f"<:success:1208885438010359869> Here's your distributor/manufacturer :) {company}",
        color=0x00FF00
    )
    await ctx.send(embed=embed)
    return
    



bot.start("TOKEN")
