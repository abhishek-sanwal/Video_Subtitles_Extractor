from django.test import TestCase

# Create your tests here.



s = '''
1
00:00:00,500 --> 00:00:02,000
<font color="#ffff00"><font size="14">www.tvsubtitles.net</font></font>

2
00:00:01,137 --> 00:00:03,104
Geez, I can't believe we found
a version of Earth

3
00:00:03,139 --> 00:00:05,306
with a "Ball Fondlers"
movie franchise.

4
00:00:05,341 --> 00:00:08,576
I can't believe the things
this reality considers PG-13.

5
00:00:08,611 --> 00:00:11,312
- Yeah. I-I'm pretty jealous.
- Don't be, Morty.

6
00:00:11,347 --> 00:00:14,215
There's pros and cons to
every alternate timeline

7
00:00:14,250 --> 00:00:15,483
fun facts about this one--

8
00:00:15,518 --> 00:00:18,353
It's got giant, telepathic
spiders, 11 9/11s,

9
00:00:18,387 --> 00:00:22,433
and the best ice cream
in the multiverse!

10
00:00:22,468 --> 00:00:25,003
- Shut up!
- We go get some ice cream, mother[bleep]!

11
00:00:27,006 --> 00:00:28,306
Oh, great.

12
00:00:28,374 --> 00:00:29,908
Oh, boy.
W-what's wrong, Rick?

13
00:00:29,942 --> 00:00:31,743
Is it the quantum carburetor
or something?

14
00:00:31,777 --> 00:00:33,878
"Quantum carburetor"?
Jesus, Morty.

15
00:00:33,913 --> 00:00:35,547
You can't just add
a--

16
00:00:35,581 --> 00:00:37,849
Sci-Fi word to a car word
and hope it means something.

17
00:00:37,883 --> 00:00:40,323
Huh, looks like something's wrong
with the microverse battery.

18
00:00:40,352 --> 00:00:43,588
- We're gonna have to go inside.
- Um, go inside what?

19
00:00:43,622 --> 00:00:45,456
The battery, Morty.
Be right back, Summer.

20
00:00:45,524 --> 00:00:46,891
Stay put,
don't touch any buttons,

21
00:00:46,959 --> 00:00:50,328
and ignore all random thoughts
that feel... spidery.

22
00:00:50,362 --> 00:00:51,763
Wait!
You can't leave me here!

23
00:00:51,797 --> 00:00:54,499
You'll be fine.
Ship, keep Summer safe.

24
00:00:54,533 --> 00:00:56,501
<i>Keep Summer safe.</i>

25
00:00:56,535 --> 00:00:57,669
Ohh!

26
00:00:59,471 --> 00:01:01,039
Ugh.
Wonderful.

27
00:01:05,477 --> 00:01:07,512
Hey, excuse me.
Hello.

28
00:01:07,580 --> 00:01:09,581
Um...

29
00:01:09,615 --> 00:01:11,583
What, you think
you're better than me?!

30
00:01:11,617 --> 00:01:13,651
Nobody's better than me!

31
00:01:13,686 --> 00:01:14,886
Hey!
Hey!

32
00:01:19,124 --> 00:01:20,925
Aah!
Aaaaah!

33
00:01:20,960 --> 00:01:22,460
<i>- Keep Summer safe.</i>
- Aaaaaaah!

34
00:01:22,528 --> 00:01:23,728
Hey, man, what the hell?!

35
00:01:23,796 --> 00:01:25,830
That was my daughter's
pediatrician! Aah!

36
00:01:25,865 --> 00:01:27,632
No, stop!
Don't kill him!

37
00:01:27,666 --> 00:01:28,967
<i>Confirmed.</i>

38
00:01:29,001 --> 00:01:30,468
Aah!

39
00:01:31,670 --> 00:01:33,338
Oh, God.
I can't feel my legs.

40
00:01:33,372 --> 00:01:34,606
Help!
Help!!

41
00:01:34,640 --> 00:01:37,342
<i>- Summer is safe.</i>
- I don't feel safe.

42
00:01:37,376 --> 00:01:39,043
<i>Confirmed.</i>

43
00:01:39,111 --> 00:01:41,412
No.

44
00:01:41,480 --> 00:01:42,981
Oh, God, help me.
Help me!

45
00:01:43,015 --> 00:01:44,983
Help me, please!
You can help me!

46
00:01:45,017 --> 00:01:48,052
♪♪

47
00:02:10,476 --> 00:02:16,476
Sync & corrections by XhmikosR
www.addic7ed.com

48
00:02:18,384 --> 00:02:20,385
Oh, man.
Where are we, Rick?

49
00:02:20,419 --> 00:02:21,819
Morty, remember
eight seconds ago

50
00:02:21,854 --> 00:02:23,454
when when you said,
"Go inside what?"

51
00:02:23,489 --> 00:02:24,923
And I said, "The battery"?

52
00:02:24,957 --> 00:02:26,624
And then we showed up here,
and I wasn't like,

53
00:02:26,692 --> 00:02:27,892
"Whoa, this is unexpected.

54
00:02:27,960 --> 00:02:29,894
This is not what I was
expecting, Morty.

55
00:02:29,962 --> 00:02:31,529
- What a perplexing mystery this is."
- All right, all right.

56
00:02:31,597 --> 00:02:33,464
We're inside the battery.
I get it.

57
00:02:33,499 --> 00:02:35,500
- You don't have to bust my balls.
- Huh, this isn't right.

58
00:02:35,534 --> 00:02:36,868
This pipe's supposed
to be sending

59
00:02:36,902 --> 00:02:39,671
20 terawatts of juice
up to the engine, Morty.

60
00:02:39,705 --> 00:02:41,506
Instead we've got... zero?

61
00:02:41,540 --> 00:02:42,807
Now what
are these people doing?

62
00:02:42,841 --> 00:02:45,143
W-w-w-whoa, people?

63
00:02:45,177 --> 00:02:46,844
It's time for some
hands-on engine repair.

64
00:02:46,912 --> 00:02:49,647
- All right, Morty, hold on to something.
- Whoa!

65
00:02:52,017 --> 00:02:53,518
Holy crap!

66
00:02:53,552 --> 00:02:54,819
I thought we were inside
your car battery, Rick.

67
00:02:54,853 --> 00:02:58,089
T-t-this is like a whole
p-planet or something.

68
00:02:58,123 --> 00:03:00,024
Thanks, Morty. I'm pretty proud
of this bad boy.

69
00:03:00,059 --> 00:03:01,426
Check it out.

70
00:03:01,493 --> 00:03:05,430
I put a spatially tessellated void
inside a modified temporal field

71
00:03:05,497 --> 00:03:07,865
until a planet developed
intelligent life.

72
00:03:07,900 --> 00:03:10,902
I then introduced that life
to the wonders of electricity,

73
00:03:10,970 --> 00:03:12,837
which they now generate
on a global scale.

74
00:03:12,871 --> 00:03:14,706
And, you know, some of it goes
to power my engine

75
00:03:14,740 --> 00:03:15,974
and charge my phone and stuff.

76
00:03:16,009 --> 00:03:18,509
You have a whole planet sitting
around making your power for you?

77
00:03:18,544 --> 00:03:19,811
That's slavery.

78
00:03:19,845 --> 00:03:21,980
It's society.
They work for each other, Morty.

79
00:03:22,014 --> 00:03:23,915
They pay each other.
They buy houses.

80
00:03:23,949 --> 00:03:25,650
They get married
and make children

81
00:03:25,684 --> 00:03:27,085
that replace them when they get
too old to make power.

82
00:03:27,119 --> 00:03:29,187
That just sounds like slavery
with extra steps.

83
00:03:29,221 --> 00:03:32,156
Ooh-la-la, someone's
gonna get laid in college.

84
00:03:32,191 --> 00:03:34,559
It appears we are
being revisited

85
00:03:34,593 --> 00:03:37,495
by the alien known as Rick,
who once gave our world

86
00:03:37,529 --> 00:03:39,597
the gift of gooble box
technology,

87
00:03:39,631 --> 00:03:42,133
which, when stomped on,
generates electricity,

88
00:03:42,167 --> 00:03:43,801
powering our homes
and businesses,

89
00:03:43,836 --> 00:03:45,503
improving our daily lives,
while safely removing

90
00:03:45,537 --> 00:03:50,108
the dangerous waste power
to a special disposal volcano.

91
00:03:50,175 --> 00:03:51,809
But why has Rick returned?

92
00:03:51,844 --> 00:03:54,445
And what will he say
when he hears the big news?

93
00:03:54,480 --> 00:03:56,080
Let's find out.

94
00:03:56,115 --> 00:03:58,483
You need to tell these people
they're in a battery, Rick.

95
00:03:58,550 --> 00:04:00,985
It's messed up.
There's caterers down there.

96
00:04:01,020 --> 00:04:03,187
Th-th-they're setting up
chafing dishes.

97
00:04:03,222 --> 00:04:04,279
Would you relax, Morty?

98
00:04:04,304 --> 00:04:06,624
There's nothing dishonest
about what we're doing.

99
00:04:06,658 --> 00:04:08,192
Now slap on these antennae.

100
00:04:08,227 --> 00:04:10,094
- These people need to think we're aliens.
- What? Why?

101
00:04:10,129 --> 00:04:14,032
Obviously you really
know nothing about car repair.

102
00:04:18,137 --> 00:04:20,138
Wait for the ramp, Morty.

103
00:04:20,172 --> 00:04:21,806
They love the slow ramp.

104
00:04:21,874 --> 00:04:24,709
Really gets their dicks hard
when they see this ramp

105
00:04:24,777 --> 00:04:27,011
just slowly extending down.

106
00:04:28,847 --> 00:04:31,282
Greetings!

107
00:04:32,751 --> 00:04:34,218
Morty, you got
to flip them off.

108
00:04:34,286 --> 00:04:36,220
I told them it means
"Peace among worlds."

109
00:04:36,288 --> 00:04:37,588
How hilarious is that?

110
00:04:44,029 --> 00:04:45,229
Coming through.

111
00:04:45,264 --> 00:04:47,498
Two real aliens walking
through here.

112
00:04:47,566 --> 00:04:49,500
Rick, our alien friend.

113
00:04:49,568 --> 00:04:51,669
Uh, Mr. President,
um, couldn't help but notice

114
00:04:51,703 --> 00:04:53,838
that you were having problems
generating power.

115
00:04:53,872 --> 00:04:56,207
That's correct.
We've evolved.

116
00:04:56,241 --> 00:04:59,677
Our most brilliant scientist,
Zeep Xanflorp,

117
00:04:59,711 --> 00:05:01,512
has developed
a source of energy

118
00:05:01,547 --> 00:05:03,281
that makes gooble boxes
obsolete.

119
00:05:04,783 --> 00:05:06,017
I would love to see it.

120
00:05:06,051 --> 00:05:08,786
[Bleep] you.
What did you say to me?!

121
00:05:08,821 --> 00:05:09,921
"[Bleep] you."

122
00:05:09,988 --> 00:05:12,790
Y-you told me
it means "much obliged".

123
00:05:12,825 --> 00:05:15,860
Oh. Right.
Uh, b-blow me.

124
00:05:15,894 --> 00:05:17,595
No, no, no.
Blow <i>me</i>.

125
00:05:21,834 --> 00:05:25,903
Zeep, you have an honored guest
from beyond the stars.

126
00:05:25,938 --> 00:05:28,858
I said 12 quantum stabilizers,
not 11.

127
00:05:28,882 --> 00:05:30,582
Fix it or it's your ass.

128
00:05:30,628 --> 00:05:32,161
Chris, I'm in the middle
of something.

129
00:05:32,196 --> 00:05:35,531
Zeep, is Rick--
The alien.

130
00:05:35,566 --> 00:05:37,033
Rick the alien.

131
00:05:37,067 --> 00:05:39,435
Rick the alien...

132
00:05:39,470 --> 00:05:41,037
Really?
You're gonna pull that move?

133
00:05:41,071 --> 00:05:42,739
I guided
your entire civilization.

134
00:05:42,773 --> 00:05:44,841
Your people have
a holiday named Ricksgiving.

135
00:05:44,875 --> 00:05:46,476
They teach kids
about me in school.

136
00:05:46,510 --> 00:05:47,677
I dropped out of school.

137
00:05:47,711 --> 00:05:49,045
It's not a place
for smart people.

138
00:05:49,079 --> 00:05:50,947
Ohhhh, snap!

139
00:05:50,981 --> 00:05:52,882
Listen to me,
you arrogant little--

140
00:05:52,916 --> 00:05:56,052
R-Rick was hoping
to see your new energy source.

141
00:05:56,086 --> 00:05:59,088
I think he could learn
a lot from you, Zeep.

142
00:05:59,123 --> 00:06:00,590
Fine.

143
00:06:00,624 --> 00:06:02,692
It's hard for people to grasp,

144
00:06:02,726 --> 00:06:05,695
but inside that container is
an infinite universe

145
00:06:05,729 --> 00:06:09,132
with a planet capable of generating
massive amounts of power.

146
00:06:09,166 --> 00:06:11,501
I call it a miniverse.

147
00:06:11,535 --> 00:06:13,569
Dumb name.

148
00:06:13,637 --> 00:06:14,971
- Excuse me?
- Nothing.

149
00:06:15,005 --> 00:06:17,140
I mean, it's hard
for us to comprehend all this.

150
00:06:17,174 --> 00:06:19,876
Would it be possible
for us to get some kind of tour

151
00:06:19,910 --> 00:06:21,744
of your miniverse
from the inside?

152
00:06:21,779 --> 00:06:23,701
This isn't a [bleep]
chocolate factory.

153
00:06:23,726 --> 00:06:24,614
I don't have time.

154
00:06:24,648 --> 00:06:27,150
Didn't you say time goes
more slowly in the miniverse

155
00:06:27,184 --> 00:06:28,651
relative to the real world?

156
00:06:28,686 --> 00:06:31,020
Yes, Chris.
Thanks for reminding me of that.

157
00:06:31,055 --> 00:06:33,556
Great president.
All right, let's go.

158
00:06:33,590 --> 00:06:35,091
Whoa-oh!

159
00:06:35,159 --> 00:06:36,259
Hold on to something.

160
00:06:37,811 --> 00:06:40,012
I put an unbounded vacuum
inside a temporal field

161
00:06:40,047 --> 00:06:41,614
until a world developed.

162
00:06:41,648 --> 00:06:43,583
I then introduced
the people of this world

163
00:06:43,617 --> 00:06:46,853
to the wonders of electricity
in the form of a device

164
00:06:46,887 --> 00:06:48,588
I call a flooble crank.

165
00:06:48,622 --> 00:06:50,022
What they don't know is

166
00:06:50,057 --> 00:06:53,192
that 80% of every crank's
energy output gets channeled

167
00:06:53,260 --> 00:06:55,728
out of the miniverse
to be used by us.

168
00:06:55,796 --> 00:06:57,296
No more gooble boxes.

169
00:06:57,331 --> 00:06:59,265
I got to tell you, Zeep,
with no disrespect,

170
00:06:59,299 --> 00:07:01,667
I really think what
you're doing here is unethical.

171
00:07:01,702 --> 00:07:03,136
- It's not cool.
- What?!

172
00:07:03,170 --> 00:07:06,105
Y-y-you got the people
on this world slaving away

173
00:07:06,140 --> 00:07:07,840
making your power.

174
00:07:07,875 --> 00:07:09,342
I mean,
that's what I call slavery.

175
00:07:09,376 --> 00:07:11,277
No, no, no,
they work for each other

176
00:07:11,311 --> 00:07:13,546
in exchange for money,
which they then--

177
00:07:13,580 --> 00:07:16,749
Well, that just sounds like
slavery with extra steps.

178
00:07:16,784 --> 00:07:20,586
Eek barba dirkle, somebody's
gonna get laid in college.

179
00:07:20,621 --> 00:07:21,888
Rick, a word?

180
00:07:21,922 --> 00:07:23,022
What the hell was that?

181
00:07:23,056 --> 00:07:24,824
I know.
"Eek barba dirkle"?

182
00:07:24,858 --> 00:07:26,626
That's a pretty
[bleep] up "ooh-la-la".

183
00:07:26,660 --> 00:07:28,294
No, what are you doing
telling this guy

184
00:07:28,328 --> 00:07:29,962
that his miniverse is
unethical?

185
00:07:29,997 --> 00:07:32,098
Do you not see
the hypocrisy here?

186
00:07:32,132 --> 00:07:34,000
Holy crap.
You're right, Morty.

187
00:07:34,067 --> 00:07:35,601
Hypocrisy.

188
00:07:35,636 --> 00:07:37,737
Somewhere on this planet,
there's got to be

189
00:07:37,771 --> 00:07:40,039
an arrogant scientist prick on the
verge of microverse technology,

190
00:07:40,107 --> 00:07:42,341
which would threaten to make
Zeep's flooble cranks obsolete,

191
00:07:42,376 --> 00:07:44,143
forcing Zeep to say
microverses are bad,

192
00:07:44,178 --> 00:07:47,046
at which point he'll realize
what a hypocrite he's being,

193
00:07:47,080 --> 00:07:49,982
his people will go back to
stomping on their gooble boxes,

194
00:07:50,017 --> 00:07:52,351
and you and I will be
on ice cream street, baby!

195
00:07:52,386 --> 00:07:54,187
Eating that mother[bleep]
ice cream!

196
00:07:54,221 --> 00:07:56,188
Slurping, slurping,
slurping it up.

197
00:07:56,990 --> 00:07:58,391
Wh-wh-why are you making
that face?

198
00:07:58,425 --> 00:07:59,859
Holy [bleep]!

199
00:07:59,893 --> 00:08:00,949
It's me.

200
00:08:00,974 --> 00:08:02,995
I've convinced the people of
this planet that I'm a traveler

201
00:08:03,029 --> 00:08:03,996
from another world.

202
00:08:04,031 --> 00:08:05,998
You don't think that's
overdoing it a little?

203
00:08:06,033 --> 00:08:07,667
I mean, you could achieve
the same effect

204
00:08:07,701 --> 00:08:08,968
with a pair of--
Never mind.

205
00:08:09,002 --> 00:08:10,403
You know what?
I shouldn't be so critical.

206
00:08:10,437 --> 00:08:11,804
I'm an alien.

207
00:08:11,839 --> 00:08:13,840
Places, please.
We're about to land.

208
00:08:17,177 --> 00:08:19,745
Too fast.

209
00:08:22,382 --> 00:08:25,718
<i>Law enforcement
converging on location.</i>

210
00:08:25,752 --> 00:08:26,986
<i>Keep Summer safe.</i>

211
00:08:27,020 --> 00:08:29,388
No! No, no!
Don't hurt anybody!

212
00:08:29,423 --> 00:08:32,391
<i>Confirm custom defense protocol--</i>

213
00:08:32,426 --> 00:08:35,194
<i>Keep Summer safe--
No physical force.</i>

214
00:08:35,229 --> 00:08:37,512
- Yes.
- <i>Processing.</i>

215
00:08:37,547 --> 00:08:40,282
Come out of the vehicle
with your hands in the air!

216
00:08:40,316 --> 00:08:42,050
<i>Scanning assailants.</i>

217
00:08:44,987 --> 00:08:47,389
<i>Psychological option detected.</i>

218
00:08:47,423 --> 00:08:49,491
<i>Gestating.</i>

219
00:08:49,525 --> 00:08:50,859
"Gestating"?

220
00:08:50,893 --> 00:08:54,462
Come out with your hands up,
or we will be forced to open fire!

221
00:08:55,631 --> 00:08:57,260
- Incoming!
- We got a device!

222
00:08:57,285 --> 00:08:58,414
Bomb! Bomb!

223
00:09:01,304 --> 00:09:02,504
Daddy?

224
00:09:02,538 --> 00:09:04,506
Oh, my God.

225
00:09:04,540 --> 00:09:06,174
- Hunter?
- Daddy?

226
00:09:06,208 --> 00:09:07,943
What the hell?

227
00:09:07,977 --> 00:09:10,278
Jesus Christ,
cease fire! Stay back!

228
00:09:10,313 --> 00:09:11,446
H-h-hunter?

229
00:09:11,480 --> 00:09:13,248
- Daddy.
- Hunter!

230
00:09:13,282 --> 00:09:15,250
Oh, my dear, sweet God, Hunter.

231
00:09:15,284 --> 00:09:16,585
Oh, my boy.
My boy.

232
00:09:16,652 --> 00:09:19,054
I'm sorry. I'm sorry.
It was all my fault.

233
00:09:19,088 --> 00:09:21,256
- I'm sorry.
- Daddy, leave the car alone.

234
00:09:21,290 --> 00:09:22,424
W-w-w-what?

235
00:09:22,491 --> 00:09:24,526
Leave the car alone.

236
00:09:24,560 --> 00:09:26,194
Hunter?
Don't--

237
00:09:26,228 --> 00:09:27,329
Oh, my God.

238
00:09:27,363 --> 00:09:29,631
Stay here, Hunter!
No!

239
00:09:29,665 --> 00:09:32,567
God, no!
Hunter!

240
00:09:34,070 --> 00:09:36,371
<i>All of you have loved ones.</i>

241
00:09:36,405 --> 00:09:39,007
<i>All can be returned.
All can be taken away.</i>

242
00:09:39,075 --> 00:09:41,309
<i>Please step away
from the vehicle.</i>

243
00:09:42,278 --> 00:09:44,613
<i>Keep Summer safe.</i>

244
00:09:44,647 --> 00:09:47,415
And if you continue
to turn your flooble cranks,

245
00:09:47,483 --> 00:09:50,118
I will bring you
other great alien advancements.

246
00:09:50,152 --> 00:09:52,454
- Hey, uh, let me ask you something.
- Yes?

247
00:09:52,488 --> 00:09:55,056
Any of your, uh, scientists
working on anything new?

248
00:09:55,124 --> 00:09:56,591
All of them.
That's their job.

249
00:09:56,626 --> 00:09:59,060
Yeah, yeah, yeah.
But I mean, like, energy-wise.

250
00:09:59,128 --> 00:10:01,496
Anyone working on, say,
a little universe in a box?

251
00:10:01,530 --> 00:10:03,632
How do you know about that?
It's top secret.

252
00:10:03,699 --> 00:10:07,569
So remember-- a crank
a day is not nearly enough.

253
00:10:07,603 --> 00:10:09,270
Crank it.

254
00:10:09,338 --> 00:10:12,107
I told them this means
"Peace among worlds".

255
00:10:12,141 --> 00:10:15,210
- How hilarious is that?
- Re-really funny, Zeep.

256
00:10:15,244 --> 00:10:17,579
Hey, Zeep, the fake president
of your fake world

257
00:10:17,613 --> 00:10:19,681
has something fake important
to show you.

258
00:10:22,151 --> 00:10:23,052
It's not much now,

259
00:10:23,077 --> 00:10:25,454
but once I learn to accelerate
the temporal field,

260
00:10:25,488 --> 00:10:27,622
I'll be able to interact
with any sentient life

261
00:10:27,657 --> 00:10:29,457
that evolves and introduce them

262
00:10:29,492 --> 00:10:32,227
to the wonders of electricity
via a pulley-based device

263
00:10:32,294 --> 00:10:33,495
I call a blooble yank.

264
00:10:33,529 --> 00:10:35,897
But what
they won't know is--

265
00:10:35,965 --> 00:10:37,666
You'll be taking
most of their energy.

266
00:10:37,700 --> 00:10:39,234
Yeah, yeah, yeah.
I get it.

267
00:10:39,268 --> 00:10:41,603
It's showtime.

268
00:10:45,374 --> 00:10:48,943
You do realize this will make
the flooble crank obsolete?

269
00:10:48,978 --> 00:10:52,280
This is wrong, Kyle.
What you're doing is wrong.

270
00:10:52,348 --> 00:10:54,582
You're basically--
This is slavery.

271
00:10:54,617 --> 00:10:57,118
You're talking about creating
a planet of slaves.

272
00:10:57,153 --> 00:11:00,455
- Told you, Zeep.
- Oh, they won't be slaves.

273
00:11:00,489 --> 00:11:02,624
They'll work for each other
and pay each other money.

274
00:11:02,658 --> 00:11:07,696
That just sounds like slavery
with ex... tra... steps.

275
00:11:07,730 --> 00:11:09,497
- What?
- Wait a minute.

276
00:11:09,532 --> 00:11:12,167
Did you create my universe?
Is my universe a miniverse?

277
00:11:12,234 --> 00:11:14,502
- Microverse!
- Uh, teenyverse.

278
00:11:14,537 --> 00:11:16,337
Ugh!
You bastard!

279
00:11:16,405 --> 00:11:18,473
Much obliged.

280
00:11:18,497 --> 00:11:20,997
- What the hell is happening?
- This is healthy, trust me.

281
00:11:21,177 --> 00:11:23,011
You're my battery, mother[bleep].

282
00:11:23,045 --> 00:11:24,312
That's all you are.

283
00:11:24,346 --> 00:11:26,314
I made you.
Your microverse sucks!

284
00:11:26,338 --> 00:11:28,938
And your miniverse is the size
of a [bleep] lobster tank!

285
00:11:28,962 --> 00:11:29,718
It's whack!

286
00:11:29,719 --> 00:11:32,020
Are they not really aliens?

287
00:11:32,088 --> 00:11:36,191
Nah, they're just a couple of crazy,
wacky scientists, you know?

288
00:11:36,225 --> 00:11:37,592
So he made a universe,

289
00:11:37,626 --> 00:11:39,294
and that guy is
from <i>that</i> universe.

290
00:11:39,328 --> 00:11:41,629
And that guy made a universe.

291
00:11:41,664 --> 00:11:45,233
And that's the universe
where I was born.

292
00:11:45,267 --> 00:11:47,469
Where my father died.

293
00:11:47,503 --> 00:11:49,704
Where I couldn't make time
for his funeral

294
00:11:49,772 --> 00:11:54,209
because I was working
on my universe.

295
00:11:54,243 --> 00:11:56,010
- I made you!
- Yeah.

296
00:11:56,045 --> 00:11:57,712
Science, huh?
Ain't it a thing.

297
00:11:57,747 --> 00:12:00,048
You know, one time,
Rick sh-- accidentally shot

298
00:12:00,082 --> 00:12:01,683
his laser pistol
right through my hand.

299
00:12:01,717 --> 00:12:05,286
You know, I mean, like,
old-lady science, you know?

300
00:12:05,321 --> 00:12:07,122
She's a real--

301
00:12:07,156 --> 00:12:08,456
You got to hang on tight,
you know?

302
00:12:08,491 --> 00:12:11,292
Because she-- she'll--
She bucks pretty hard.

303
00:12:11,327 --> 00:12:14,329
Ooh, boy, what--
Oh, my God, no!

304
00:12:19,301 --> 00:12:20,435
- Teenyverse.
- Teenyverse.

305
00:12:22,152 --> 00:12:24,119
Come on, come on, come on.

306
00:12:24,154 --> 00:12:25,254
Pterodactyl!

307
00:12:25,989 --> 00:12:27,290
Asshole!

308
00:12:27,324 --> 00:12:28,925
When I get
out of this teenyverse,

309
00:12:28,959 --> 00:12:30,827
I'm gonna smash it to pieces
with you in it.

310
00:12:30,861 --> 00:12:32,562
Yeah, well, when I get
out of this teenyverse,

311
00:12:32,596 --> 00:12:34,430
I'm gonna get out of
the surrounding miniverse

312
00:12:34,465 --> 00:12:36,399
and then the microverse
around that, and guess what?

313
00:12:36,433 --> 00:12:37,900
Don't make things worse, Rick!

314
00:12:37,935 --> 00:12:39,902
Uh, he's not gonna destroy
your universe.

315
00:12:39,937 --> 00:12:41,904
You know, we--
We need it to start our car.

316
00:12:41,939 --> 00:12:44,273
That's what you used
my universe for?

317
00:12:44,308 --> 00:12:45,942
To run your car?

318
00:12:45,976 --> 00:12:47,343
Yeah, but don't
flatter yourself.

319
00:12:47,378 --> 00:12:50,079
There's always AAA,
you [bleep] [bleep]sucker!

320
00:12:51,148 --> 00:12:53,015
What's he doing?
What's he crafting?

321
00:12:53,050 --> 00:12:54,517
I can craft stuff, too, pal!

322
00:12:54,551 --> 00:12:56,386
Just like I crafted
your reality!

323
00:12:57,654 --> 00:12:59,055
You crafty son of a--

324
00:12:59,089 --> 00:13:00,289
Ow!

325
00:13:00,324 --> 00:13:03,926
I crafted the guy that created
the planet you're standing on!

326
00:13:03,961 --> 00:13:06,362
Yeah, and I made the stars that became
the carbon in your mother's ovaries!

327
00:13:06,397 --> 00:13:08,164
I didn't ask to be born!

328
00:13:08,198 --> 00:13:09,599
All right, that's it!
I'm out.

329
00:13:09,633 --> 00:13:11,467
I-I'm gonna go
into the wilderness,

330
00:13:11,502 --> 00:13:14,470
and I'm gonna make a new life for
myself among the tree people.

331
00:13:14,505 --> 00:13:16,906
- It can't be worse than this.
- Sure. Okay, Morty.

332
00:13:16,940 --> 00:13:19,342
Just be back before sundown
or the tree people will eat you.

333
00:13:19,409 --> 00:13:20,376
That's a myth!

334
00:13:20,411 --> 00:13:22,311
W-w-why are you trying
to start a myth?

335
00:13:22,346 --> 00:13:23,880
It's a prehistoric planet, Morty.

336
00:13:23,947 --> 00:13:25,448
Someone has to bring
a little culture.

337
00:13:25,482 --> 00:13:27,116
And it certainly can't be someone

338
00:13:27,151 --> 00:13:30,286
whose entire culture powers
my brake lights!

339
00:13:32,923 --> 00:13:34,856
Go, go, go!

340
00:13:35,856 --> 00:13:37,857
Oh, my God.
Oh, God.

341
00:13:37,881 --> 00:13:39,581
What are we going to do now?

342
00:13:39,592 --> 00:13:42,427
<i>I am unable
to destroy this army.</i>

343
00:13:42,461 --> 00:13:45,864
<i>To clarify, I am quite able
to destroy this army,</i>

344
00:13:45,898 --> 00:13:48,132
- <i>but you will not permit it.</i>
- Correct.

345
00:13:48,200 --> 00:13:51,502
<i>You also refuse to authorize
emotional countermeasures.</i>

346
00:13:51,537 --> 00:13:54,505
If you're talking
about the melting ghost babies,

347
00:13:54,540 --> 00:13:56,474
yes, please, no more of that.

348
00:13:56,508 --> 00:13:58,476
<i>Confirmed.</i>

349
00:13:58,536 --> 00:14:01,536
<i>I am currently constructing
a security measure</i>

350
00:14:01,547 --> 00:14:03,414
<i>in compliance
with your parameters.</i>

351
00:14:03,449 --> 00:14:06,751
<i>But I do want to say
you are not making this easy.</i>

352
00:14:06,819 --> 00:14:08,353
You know you're
kind of a dick, right?

353
00:14:08,387 --> 00:14:11,389
<i>My function is
to keep Summer safe,</i>

354
00:14:11,423 --> 00:14:14,525
<i>not keep Summer being,
like, totally stoked</i>

355
00:14:14,560 --> 00:14:17,462
<i>about, like,
the general vibe and stuff.</i>

356
00:14:17,496 --> 00:14:20,164
<i>That's you.
That's how you talk.</i>

357
00:14:23,702 --> 00:14:26,171
Hey, that's my deer!

358
00:14:27,706 --> 00:14:29,174
Aaaaaaah!

359
00:14:29,208 --> 00:14:30,508
Raah!

360
00:14:30,576 --> 00:14:33,611
I hope your God is
as big a dick as you.

361
00:14:36,649 --> 00:14:39,250
My God's the biggest dick
that's never existed.

362
00:14:39,285 --> 00:14:41,152
Why do you think I'm even here?

363
00:14:43,532 --> 00:14:45,198
You're here

364
00:14:45,233 --> 00:14:47,401
because you created
someone smarter than you.

365
00:14:49,804 --> 00:14:53,373
Oh, I thought we were both here because
I created a universe of idiots.

366
00:14:59,847 --> 00:15:02,449
Kalo kada sha la.

367
00:15:02,483 --> 00:15:03,583
Holy shit.
Morty?

368
00:15:03,618 --> 00:15:05,252
I haven't seen you in months.

369
00:15:05,286 --> 00:15:06,820
You're leading the tree people?

370
00:15:06,854 --> 00:15:08,288
Huh.
That's a step up.

371
00:15:08,322 --> 00:15:09,489
We have no leaders.

372
00:15:09,557 --> 00:15:12,125
We follow
only the will of the forest.

373
00:15:12,160 --> 00:15:13,293
Ooh. Wow.

374
00:15:13,327 --> 00:15:16,363
- Gaaaaay.
- That is pretty gay.

375
00:15:16,397 --> 00:15:18,231
You two call yourselves
geniuses,

376
00:15:18,266 --> 00:15:20,867
but you have spent
this time learning nothing.

377
00:15:20,902 --> 00:15:22,769
Come with me into the forest.

378
00:15:22,804 --> 00:15:25,338
There is something
I wish to teach you.

379
00:15:28,743 --> 00:15:32,379
This is ku'ala,
the spirit tree.

380
00:15:32,413 --> 00:15:34,347
For generations,
it has guided the--

381
00:15:35,550 --> 00:15:37,684
You have to get us
the [bleep] out of here.

382
00:15:37,718 --> 00:15:39,553
These people are
backwards savages.

383
00:15:39,587 --> 00:15:41,188
They eat every third baby

384
00:15:41,222 --> 00:15:43,356
because they think
it makes fruit grow bigger.

385
00:15:43,391 --> 00:15:45,892
Everyone's gross, and they all
smell like piss all the time.

386
00:15:45,927 --> 00:15:48,495
I m-- I miss my family.
I miss my laptop.

387
00:15:48,563 --> 00:15:51,765
I masturbated to an extra-curvy
piece of driftwood the other day!

388
00:15:51,799 --> 00:15:53,500
Look, I don't care
what it takes.

389
00:15:53,534 --> 00:15:55,202
You two are putting aside
your bull[bleep],

390
00:15:55,236 --> 00:15:57,571
and you're working together
to get us back home.

391
00:15:57,605 --> 00:15:59,506
No can do, Morty.
I just can't.

392
00:15:59,540 --> 00:16:01,341
I just don't see how I can--

393
00:16:01,375 --> 00:16:02,642
Ro ro dah no gah!

394
00:16:02,677 --> 00:16:05,412
You're smart.
You'll figure it out.

395
00:16:05,446 --> 00:16:09,549
You have 10
seconds to get out of the ship!

396
00:16:09,584 --> 00:16:11,485
10, 9...

397
00:16:12,487 --> 00:16:13,753
All right, not bad.

398
00:16:13,788 --> 00:16:15,856
I guess you're
an okay proto recombinator.

399
00:16:15,923 --> 00:16:18,458
I've certainly seen
worse ionic cell dioxination.

400
00:16:18,493 --> 00:16:20,160
If this works,
drinks are on me.

401
00:16:20,194 --> 00:16:21,862
If drinks are on you,
you're gonna need

402
00:16:21,929 --> 00:16:23,597
a second mortgage
on that tower.

403
00:16:23,631 --> 00:16:25,132
I'm an alcoholic.

404
00:16:25,199 --> 00:16:26,700
Opium addict.

405
00:16:28,936 --> 00:16:31,538
All right, okay, okay,
okay, wrap it up.

406
00:16:31,606 --> 00:16:34,441
You guys are the [bleep] worst!
Your gods are a lie!

407
00:16:34,509 --> 00:16:36,943
[Bleep] you, [bleep] nature,
and [bleep] trees!

408
00:16:39,514 --> 00:16:40,747
Yes! You did it!
Yes!

409
00:16:40,781 --> 00:16:42,516
Hey, uh, how about that drink?

410
00:16:42,550 --> 00:16:45,619
Sure, I just need to go grab
my wallet from inside my ship.

411
00:16:45,653 --> 00:16:47,187
Isour wallet in your ship?

412
00:16:47,255 --> 00:16:50,223
That's where the transporter is,
too, so why don't we come with?

413
00:16:50,258 --> 00:16:53,437
It's cool.
I'll be back in a sec.

414
00:16:53,472 --> 00:16:56,941
You know how long a second can
take in a microverse?

415
00:16:56,975 --> 00:16:58,976
Oh!
Run, Morty!

416
00:16:59,011 --> 00:17:01,312
That asshole's willing to risk everything
he cares about just to defeat me!

417
00:17:01,346 --> 00:17:02,480
He's psychotic!

418
00:17:05,384 --> 00:17:07,685
- Morty, hop on my back.
- Why?

419
00:17:07,719 --> 00:17:10,054
Go, go Sanchez ski shoes.

420
00:17:11,757 --> 00:17:13,891
Aaaaaah!
...Eight...

421
00:17:15,027 --> 00:17:16,327
Aaaah!
Oof!

422
00:17:17,729 --> 00:17:19,697
Hold still.

423
00:17:20,999 --> 00:17:24,669
Oh, hey, guys. I just
finished cooking us a feast.

424
00:17:24,703 --> 00:17:26,470
Aaaah!
Holy--

425
00:17:26,505 --> 00:17:28,673
- You monster!
- Whoa. Bad tour.

426
00:17:28,707 --> 00:17:30,374
...seven...

427
00:17:30,442 --> 00:17:32,009
Hey, you got to sign out.

428
00:17:32,077 --> 00:17:34,545
Nothing you do matters!
Your existence is a lie!

429
00:17:34,613 --> 00:17:38,382
If that were
really true, then...

430
00:17:38,450 --> 00:17:40,451
- I'm here to see Ron Mendleson.
- Third floor.

431
00:17:40,485 --> 00:17:41,986
Would you like
to go to dinner with--

432
00:17:42,020 --> 00:17:43,788
Uh, no.

433
00:17:46,458 --> 00:17:49,927
You may have created this
universe, Rick, but I live in it.

434
00:17:49,962 --> 00:17:51,462
[Bleep]

435
00:17:51,496 --> 00:17:53,631
What are we gonna do, Rick?
We're so screwed.

436
00:17:53,665 --> 00:17:55,066
He's gonna get to the
ship and smash the microverse,

437
00:17:55,091 --> 00:17:56,091
and then he's gonna kill us!

438
00:17:56,134 --> 00:17:57,660
Quick, Morty, you've
got to turn into a car.

439
00:17:57,685 --> 00:17:58,169
What?!

440
00:17:58,203 --> 00:18:00,604
A long time ago, I implanted you
with a subdermal chip

441
00:18:00,672 --> 00:18:03,107
that could call upon dormant
nanobots in your bloodstream

442
00:18:03,141 --> 00:18:05,509
to restructure your anatomy
and turn you into a car.

443
00:18:05,544 --> 00:18:06,777
- Oh, my God!
- Concentrate, Morty.

444
00:18:06,812 --> 00:18:08,332
Concentrate and turn
into a car, Morty.

445
00:18:09,815 --> 00:18:11,615
Never mind. Here's a taxi.
Get in. It's fine.

446
00:18:11,650 --> 00:18:13,117
...six...

447
00:18:15,821 --> 00:18:16,954
- Hey, Zeep.
- Huh?

448
00:18:16,989 --> 00:18:19,690
Happy Ricksgiving, biiiiiitch.

449
00:18:19,725 --> 00:18:21,826
Aaah!

450
00:18:21,860 --> 00:18:23,527
We did it, Morty.

451
00:18:23,562 --> 00:18:25,096
Now let's get out of here
and destroy this whole universe.

452
00:18:25,130 --> 00:18:26,464
Excuse me?

453
00:18:26,498 --> 00:18:27,898
...five--

454
00:18:27,933 --> 00:18:29,600
Sir?

455
00:18:31,503 --> 00:18:32,937
- Holy hell.
- Sir!

456
00:18:34,106 --> 00:18:35,206
Hold you fire!

457
00:18:37,976 --> 00:18:39,744
What's going on?

458
00:18:39,778 --> 00:18:41,512
<i>I have brokered
a peace agreement</i>

459
00:18:41,546 --> 00:18:43,614
<i>between the giant spiders
and the government.</i>

460
00:18:43,648 --> 00:18:47,051
Thanks to the skilled diplomacy
of this mysterious space car,

461
00:18:47,085 --> 00:18:49,987
from this day forward,
human- and spiderkind will live

462
00:18:50,022 --> 00:18:51,856
side by side in peace.

463
00:18:51,923 --> 00:18:54,692
We will stop bombing them,
and they will no longer use

464
00:18:54,726 --> 00:18:56,761
their telepathic abilities
to make us wander into webs

465
00:18:56,828 --> 00:18:58,462
for later consumption.

466
00:18:58,497 --> 00:19:00,564
Instead, we will work together
to make this world

467
00:19:00,599 --> 00:19:04,602
a better place for all,
no matter how many legs.

468
00:19:04,669 --> 00:19:06,771
What do we do
about the space car?

469
00:19:06,838 --> 00:19:08,139
Leave it alone.

470
00:19:08,173 --> 00:19:09,807
I mean, what did it
really do, anyways?

471
00:19:09,841 --> 00:19:11,108
Kill a guy
and paralyze his buddy?

472
00:19:11,143 --> 00:19:14,011
Not a bad trade
for spider peace.

473
00:19:14,046 --> 00:19:15,980
All right, that's it.
Move out!

474
00:19:20,886 --> 00:19:23,721
I love this spider!

475
00:19:23,789 --> 00:19:25,489
<i>Summer is safe.</i>

476
00:19:25,524 --> 00:19:26,991
All right, I get it.

477
00:19:31,029 --> 00:19:32,229
Rick!

478
00:19:33,999 --> 00:19:35,566
Don't do it.

479
00:19:35,600 --> 00:19:38,869
You quit school, but you
still got some learning to do.

480
00:19:51,049 --> 00:19:52,683
Aah!

481
00:19:52,717 --> 00:19:54,118
Unh!

482
00:20:02,928 --> 00:20:04,995
Class dismissed.

483
00:20:05,030 --> 00:20:07,264
Geez.

484
00:20:15,941 --> 00:20:17,508
- You all right?
- Uh-huh!

485
00:20:17,576 --> 00:20:18,776
What are you doing, Rick?

486
00:20:18,844 --> 00:20:20,544
I'm pretty sure
the battery's dead.

487
00:20:20,579 --> 00:20:21,879
Oh, you think so, huh, Morty?

488
00:20:21,947 --> 00:20:23,080
Well, let's see.

489
00:20:23,115 --> 00:20:25,983
Hey, wait-- huh?
I don't get it.

490
00:20:26,017 --> 00:20:28,252
Of course you don't.
But Zeep did.

491
00:20:28,320 --> 00:20:29,854
He knew that once I got
back to my car,

492
00:20:29,888 --> 00:20:31,789
one of two things
was gonna happen--

493
00:20:31,823 --> 00:20:33,858
I was gonna have to toss
a broken battery,

494
00:20:33,892 --> 00:20:36,727
or the battery wouldn't
be broken.

495
00:20:41,166 --> 00:20:45,035
Peace among worlds, Rick.

496
00:20:45,103 --> 00:20:46,237
Jesus.

497
00:20:46,271 --> 00:20:48,572
Yeah.
Listen to that baby purr.

498
00:20:48,607 --> 00:20:49,374
You were right, Morty--

499
00:20:49,399 --> 00:20:51,142
We really just needed to
be honest with those guys.

500
00:20:51,176 --> 00:20:52,376
All right, here we go.

501
00:20:54,980 --> 00:20:56,814
Thank y-o-o-ou.

502
00:20:56,848 --> 00:20:58,816
See, Morty?
This is what it's all about.

503
00:20:58,850 --> 00:21:00,284
This is why we do what we do.

504
00:21:00,318 --> 00:21:01,785
- Uh-huh.
- Ew! What the hell?

505
00:21:01,853 --> 00:21:03,954
Jesus!
There's flies in my ice cream.

506
00:21:03,989 --> 00:21:05,222
Presidential decree--

507
00:21:05,257 --> 00:21:09,326
All ice cream is now for all beings,
no matter how many legs.

508
00:21:09,361 --> 00:21:11,428
- What the [bleep] did you do, Summer?!
- It was your ship!

509
00:21:11,463 --> 00:21:13,063
- Your stupid ship did it!
- Don't blame my ship!

510
00:21:13,098 --> 00:21:14,932
- It melted a child!
- My ship doesn't do anything...

511
00:21:14,999 --> 00:21:16,467
- It killed it itself!
- ...unless it's told to do something!

512
00:21:16,501 --> 00:21:18,341
- We almost died!
- I don't want to hear it, Summer!

513
00:21:18,370 --> 00:21:20,404
Your boobs are all hanging about,

514
00:21:20,472 --> 00:21:22,373
and you ruined ice cream
with your boobs out.

515
00:21:22,407 --> 00:21:24,108
And don't even try
to deny it, either.

516
00:21:25,366 --> 00:21:31,366
Sync & corrections by XhmikosR
www.addic7ed.com

517
00:22:14,293 --> 00:22:15,293
<i>Did you get any of that?</i>

518
00:22:15,594 --> 00:22:20,031
<i>It's a good show.</i>
'''
import re
pattern =r"^<.*>$"
arr = s.split("\n\n")
pattern =r"^<.*>$"
pattern2 = r"^<.*[/>]$"

for i in arr:
    num, time, *content = i.strip().split("\n")
    
    for word in content:
            
        word = re.sub(pattern,"",word)
        word = re.sub(pattern2,"",word)
        print(word,"Brackets removed")