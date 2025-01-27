from discord.ext import commands, tasks
import dbl

from LichessBot import LichessBot


class TopGG(commands.Cog):
    """
    TopGG API Cog:
    https://top.gg/bot/707287095911120968
    """
    def __init__(self, client: LichessBot):
        self.client = client
        self.logger = self.client.logger
        self.token = self.client.config.top_gg_token
        self.dblpy = dbl.DBLClient(self.client, self.token)
        self.update_stats.start()

    @tasks.loop(hours=4)
    async def update_stats(self):
        """
        Update server count every 4 hours
        @return:
        """
        self.logger.debug('Attempting to post server count...')
        try:
            await self.dblpy.post_guild_count()
            self.logger.debug(f'Posted server count ({self.dblpy.guild_count()})')
        except Exception as e:
            self.logger.exception(f'Failed to post server count\n{type(e).__name__}: {e}')


def setup(client: LichessBot):
    client.add_cog(TopGG(client))
    client.logger.info("Sucessfully added cog: TopGG")
