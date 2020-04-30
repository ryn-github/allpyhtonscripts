import re

st = '''Well, you can tell by the way I use my walk
I'm a woman's man, no time to talk
Music loud and women warm
I've been kicked around since I was born
But now it's all right, that's okay
You may look the other way
We can try to understand
The New York Times' effect on man
Whether you're a brother or whether you're a mother
You're stayin' alive, stayin' alive
Feel the city breakin' and everybody shakin'
I'm a-stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' ali-i-i-i-ive
Oh, when you walk
Well, now I get low and I get high
And if I can't get either, I really try
Got the wings of heaven on my shoes
I'm a dancin' man, and I just can't lose
You know, it's all right, it's okay
I'll live to see another day
We can try to understand
The New York Times' effect on man
Whether you're a brother or whether you're a mother
You're stayin' alive, stayin' alive
Feel the city breakin' and everybody shakin'
I'm a-stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' ali-i-i-i-ive
Oh
Life goin' nowhere, somebody help me
Somebody help me, yeah
Life goin' nowhere, somebody help me, yeah
I'm stayin' alive
Well, you can tell by the way I use my walk
I'm a woman's man, no time to talk
Music loud and women warm
I've been kicked around since I was born
Now it's all right, it's okay
You may look the other way
We can try to understand
The New York Times' effect on man
Whether you're a brother or whether you're a mother
You're stayin' alive, stayin' alive
Feel the city breakin' and everybody shakin'
I'm a-stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' alive, stayin' alive
Ah, ah, ah, ah, stayin' ali-i-i-i-ive
Yeah
Life goin' nowhere, somebody help me
Somebody help me, yeah
Life goin' nowhere, somebody help me, yeah
I'm stayin' ali-i-i-i-ive
Life goin' nowhere, somebody help me
Somebody help me, yeah
Life goin' nowhere, somebody help me, yeah
I'm stayin' ali-i-i-i-ive
Life goin' nowhere, somebody help me
Somebody help me, yeah
Life goin' nowhere, somebody help me, yeah
I'm stayin' ali-i-i-i-ive
Life goin' nowhere, somebody help me
Somebody help me, yeah
Life goin' nowhere, somebody help me, yeah
I'm stayin' ali-i-i-i-ive'''

store = re.compile(r'(ali)(ve)')

# re.compile(r'') is used to specify the pattern to look for in a string
# it creates and object of the pattern

serch = store.search(st)
print(serch)

# object.search(input) can be used on the obect to
# search for the pattern, returns an object value


print(serch.group())

# obj.group(value) can be used to return specific patterns
# the first pattern inside the first set of brackets is group 1
# second set is group 2 and so on


alreg = re.compile(r'(alive|ali-i-i-i-ive)')

# pipe character works like and or statement
# check for first or second pattern 

# assigned after a group
# question mark - pattern should appear one or zero times

# * - pattern should apper zero or more times
# + - one or more times
# {number} - specific number of repititions

# {x,y} - atleast x, max y
# by default, python matches the maximum length of the string
# {}? tells python to match shortes string

# {} - no minumum or maximum

alserch = alreg.findall(st)

# if search was not able to find the pattern
# it returns none

print(alserch)