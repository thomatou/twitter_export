import keys
import twitter
import datetime as dt


class Get_Posts:
"""
Authentication is not required for searching a public user's timeline
Authentication is required for searches of private users
"""
    def __init__(self,
                API_key,
                API_secret_key,
                access_token,
                access_token_secret):

        self.API_key = API_key
        self.API_secret_key = API_secret_key
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self.api = twitter.Api(self.API_key,
                          self.API_secret_key,
                          self.access_token,
                          self.access_token_secret)

    def to_timestamp(self, s):
        """ Converts twitter created_at object to a UNIX timestamp """

        return float(dt.datetime.strptime(s, '%a %b %d %H:%M:%S %z %Y').timestamp())

    def binary_search(self, tweets, bottom, top, start_time):
        """
        Search through a date-sorted list of tweets for the first one that
        matches the specified date.
        When calling the function, tweets should be a list of tweet objects
        as returned by the twitter API, bottom should be set to 0, and
        top should be set to len(tweets)
        """

        if self.to_timestamp(tweets[0].created_at) < start_time:
            return
        else:
            return tweets

        mid = (bottom + top) // 2

        if self.to_timestamp(tweets[mid].created_at) > start_time:
            if self.to_timestamp(tweets[mid + 1].created_at) < start_time:
                # print('found!', mid)
                return tweets[:mid+1]

            else:
                # print(bottom, top, 'tweets[' + str(mid) + ':]')
                return self.binary_search(tweets, mid+1, top, start_time)

        if self.to_timestamp(tweets[mid].created_at) <= start_time:
            # print(bottom, top, 'tweets[:' + str(mid) + ']')
            return self.binary_search(tweets, bottom, mid-1, start_time)

    def fetch_posts(self, user, year, month, day):
        start_time = dt.datetime(year,month,day, tzinfo=dt.timezone.utc).timestamp()
        tweets = []

        statuses = self.api.GetUserTimeline(screen_name=user,
                                            count=200)

        tweets.extend(sorted(statuses, key=lambda x: x.id, reverse=True))

        earliest_post = tweets[-1]

        new_early = self.to_timestamp(earliest_post.created_at)


        counter = 0
        while new_early > start_time:
            statuses = self.api.GetUserTimeline(screen_name=user,
                                                max_id=tweets[-1].id,
                                                count=200)
            if statuses:

                temp = sorted(statuses, key=lambda x: x.id, reverse=True)

                earliest_post = temp[-1]

                new_early = self.to_timestamp(earliest_post.created_at)

                if earliest_post.id == tweets[-1].id:
                    break

                tweets.extend(temp)

            else:
                print('no statuses to report')
                break

            print(counter)
            counter += 1

        trimmed_tweets = self.binary_search(tweets, 0, len(tweets), start_time)

        if not trimmed_tweets:
            return 'No posts since then!'

        return trimmed_tweets




test = Get_Posts(keys.API_key, keys.API_secret_key, keys.access_token, keys.access_token_secret).fetch_posts('@realDonaldTrump', 2019, 6, 1)

print(test)

#
# Get_Posts(keys.API_key, keys.API_secret_key, keys.access_token, keys.access_token_secret).binary_search(test,0,len(test),1590969600.0)
#
# Get_Posts(keys.API_key, keys.API_secret_key, keys.access_token, keys.access_token_secret).to_timestamp(2020,6,1)
