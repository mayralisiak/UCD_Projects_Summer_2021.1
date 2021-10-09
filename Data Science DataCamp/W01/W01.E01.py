nums = [2,4,6,8,10]
result = map(lambda a: a**2,nums)
print(result)

spells = ["protego", "accio", "expecto patronum", "legilimens"]

shout_spells = map(lambda item: item + '!!!', spells)
shout_spells_list = list(shout_spells)
print(shout_spells_list)

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)
result_list.sort()
print(fellowship)
print(result_list)


result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
res_list = list(result)
for tweet in res_list:
    print(tweet)

def shout_echo(word1, echo=1)
    """Concatenete acho copies of word1 and three exclamation marks at the end of the string."""

echo_word = ""
shout_words = ""

    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except:
        print("word1 must be a string and echo must be an integer.")

    return shout_words

shout_echo('particle', echo="accelerator")

def shout_echo(word1, echo=1):

    if echo <= 0:
        raise ValueError('echo must be greater than or equal to 0')
    echo_word = word1 * echo
    shout_word = echo_word + "!!!"

    return shout_word

shout_echo("particle", echo=5)