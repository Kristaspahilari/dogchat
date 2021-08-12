from datetime import datetime



comment1 = {
    "Text" : "What time are you going?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 0, 0),
}

comment2 = {
    "Text" : "I'm going to go at 7 tonight!",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 30, 0),
}

comment3 = {
    "Text" : "You bet!  I love naps.",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 6, 29, 9, 30, 0),
}

comment4 = {
    "Text" : "What treats do you like the best?",
    "Name": "bubi",
    "Username" : "bubi12",
    "Picture" : "bub.jpg",
    "DateTime" : datetime(2021, 6, 30, 14, 30, 0),
}

post1 = {
    "PostId" : 1,
    "Text": "I can't wait to go to the park today",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": ["charlie"],
    "Comments" : [comment1, comment2],
    "DateTime" : datetime(2021, 7, 1, 17, 0, 0),
    "Picture" : "melba_profile.png"
}

post2 = {
    "PostId" : 2,
    "Text": "I could really use a treat right now",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": ["charlie"],
    "Comments" : [comment4],
    "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
    "Picture" : "melba_profile.png"
}

post3 = {
    "PostId" : 3,
    "Text": "Arent' naps the best?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Likes": ["melba"],
    "Comments" : [comment3],
    "DateTime" : datetime(2021, 6, 29, 9, 0, 0),
    "Picture" : "charlie_profile.png"

}
post4 = {
    "PostId" : 4,
    "Text": "I love this app!",
    "Name": "bubi",
    "Username" : "bubi12",
    "Likes": ["charlie"],
    "Comments" : [],
    "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
    "Picture" : "bub.jpg"
}

test_posts = {
    1 : post1,
    2 : post2,
    3 : post3,
    4 : post4
}

melba_posts = {
    1 : post1,
    2 : post2
}

charlie_posts = {
    3 : post3
}
bubi_posts = {
    4 : post4
}

charlie = {
    "Name": "Charlie",
    "Bio" : "Hi, I'm Charlie!  I'm a standard poodle and I love to nap.",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "Birthday" : datetime(2018, 1, 2),
    "Posts" : charlie_posts
}

melba = {
    "Name": "Melba",
    "Bio" : "My name is Melba. I'm a miniature golden-doodle.  My favorite place in the world is Discovery Park in Seattle, Washington.",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "Birthday" : datetime(2013, 2, 14),
    "Posts": melba_posts
}

bubi = {
    "Name": "Bubi",
    "Bio" : "Hi, I'm  Bubi! I like treats and long walks!",
    "Username" : "bubi12",
    "Picture" : "bub.jpg",
    "Birthday" : datetime(2019, 3, 5),
    "Posts" : bubi_posts
}

dogs = {
    "melba" : melba,
    "chucky" : charlie,
    "bubi12" : bubi
}