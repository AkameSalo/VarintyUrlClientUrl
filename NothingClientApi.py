import asyncio
import httpx

from tokens import self_token


class NothingApi:
    """Nothing Discord bot async lib
    Last Date Edit 30.06.2023 11:38
    >>> NothingApi(api_version='v9')
    """

    def __init__(self, discord_api_version: str = 'v9') -> None:
        self.discord_api_version = discord_api_version

    # Custom Exceptions
    class ArgumentsError(Exception):
        pass

    class AuthorizationError(Exception):
        pass

    class InvalidOrTakenException(Exception):
        pass

    class MissingPermissions(Exception):
        pass

    async def changeVarintyUrl(self, guild_id: int, varinty_symbols: str, token: str) -> httpx.Response:
        """Change varinty guild url"""
        async with httpx.AsyncClient() as client:
            if varinty_symbols and token and guild_id:
                headers = {
                    'content-type': 'application/json',
                    'Authorization': token,
                }
                request = await client.patch(url=f"https://discord.com/api/{self.discord_api_version}/guilds/{guild_id}/vanity-url", headers=headers, json={"code": varinty_symbols})
                request_code = dict(request.json()).get('code', None)

                if request_code == 0:
                    raise self.AuthorizationError('Authorization Exception')

                if request_code == 50020:
                    raise self.InvalidOrTakenException('Invite code is either invalid or taken.')

                if request_code == 50013:
                    raise self.MissingPermissions('Missing Permissions')

                else:
                    return request

            else:
                raise self.ArgumentsError("Invalid arguments provided")


# Consts
GUILD_ID: int = 1089472640873402441     # nothing Guild ID
GUILD_VARINTY_CODE: str = 'nthg'

self_token = 'ASDFJSDF.SDFWEFW.ZXFASDF.WDFW-WDFWDFSDF.EFWEFWEFASQDQWCVEFVRWEFWEFSD43R2223F2FEFF'


# :TODO Procedure test func. This Code is Example
async def example_func() -> None:
    discord_api = NothingApi()
    try:
        await discord_api.changeVarintyUrl(GUILD_ID, GUILD_VARINTY_CODE, self_token)

    except discord_api.AuthorizationError:
        print('Поменяйте токен бота!!!!!!!')
        return


asyncio.run(example_func())
