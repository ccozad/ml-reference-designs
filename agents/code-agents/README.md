# Dependencies

You will need all of the following dependencies to run this example:

 - Hugging Face token
 - Python virtual environment

## Hugging Face token

Log in to Hugging Face and retrieve your token from https://hf.co/settings/tokens

Create an environment file named `.env`. Add the following line to your environment file:

```ini
HF_TOKEN=<your token>
```

## Python Virtual Environment

 - Move to the hello world folder
   - `cd <agents/code-agents>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

# Running the code

## Playlist agent

Run the command `python playlist_agent.py`. This will initialize.

```text
python playlist_agent.py
╭──────────────────────────────────────────────────────────────── New run ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                          │
│ Search for the best music recommendations for a wedding.                                                                                 │
│                                                                                                                                          │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ───────────────────────────────────────────────────────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  search_results = web_search(query="best music recommendations for a wedding")                                                             
  print(search_results)                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
## Search Results

[The Best Wedding Songs for Each Moment of Your Big Day - The Knot](https://www.theknot.com/content/best-wedding-songs)
Best Wedding Songs By Genre; Best Wedding Songs By Decade; Best Wedding Songs: Expert Picks. When choosing your ceremony music selections or
making a wedding dance floor playlist, some songs simply belong on the wedding soundtrack for your big day. We asked professional DJs for   
their top picks. From romantic classics to modern melodies, these ...

[Top Wedding Reception Songs | Play the Best Wedding Music - The Knot](https://www.theknot.com/content/billboard-most-popular-wedding-songs)
Our editors have rounded up the best wedding music songs, from classic hits to new unique tunes, that'll inspire your reception setlist. And
whether you hire a wedding band or ask your wedding DJ about a special wedding song request, your chosen wedding expert will have your      
guests on the dance floor all night long with these editor-approved selections.

[40 Must-Have Wedding Songs to Keep Guests Dancing (and Which ... - GigSalad](https://www.gigsalad.com/blog/must-have-wedding-songs/)       
Upbeat Wedding Reception Songs. Picking the perfect playlist for your big day is all about setting the right vibe. Energize the crowd with  
upbeat entrance music and charm them with classic tunes. Here are some of the best songs to play across different genres to keep the dance  
floor packed. And a few that may be more fitting on the no-play list.

[200 Best Wedding Reception Dance Songs Ever (2025) - PA Unveiled](https://paunveiled.com/best-wedding-reception-dance-songs/)
The best songs for parents entrance at wedding receptions. 145 funny songs to use for your garter removal and bouquet toss. 200 pre-wedding 
songs for your getting-ready morning playlist. The 57 important questions that you should ask a wedding DJ. Funny songs to use for the      
dollar dance. Best songs for the anniversary dance at your wedding ...

[162 Wedding Ceremony Songs to Create Your Music Playlist - The Knot](https://www.theknot.com/content/wedding-ceremony-songs)
First, keep in mind that some venues, like churches, have strict guidelines on what songs are played, so that will impact your song choice. 
... The Best Wedding Ceremony Songs. Every couple has that one special song. The best wedding ceremony songs are those that bring fond      
memories to you and your partner whenever you hear them. These ultra ...

[Wedding Songs: Best Tunes For Each Moment [+ Songs To Skip]](https://www.weddingforward.com/wedding-songs/)
Wedding music cannot be quite overlooked no matter the style of the wedding. But after all, that said, the choice of wedding songs depends  
on you. It's your day and your happiness, choices, and needs come first. Yet, we are all about helping you make the best of your wedding day
through good music.

[300 Best Wedding Songs for Each Moment of your Wedding Day](https://www.zola.com/expert-advice/best-wedding-songs)
Indie Wedding Songs; Gospel Wedding Songs; Best Wedding Songs by Activity. Your wedding day will include a variety of different moments and 
activities, each calling for its own type of music (ie. you wouldn't use the same tunes from your getting ready playlist for your wedding   
processional music!). Browse the list below for the best wedding ...

[129 Best Wedding Songs: from Upbeat and Fun to Romantic and Slow](https://www.functioncentral.co.uk/best-wedding-songs)
69 Last Dance Songs for Your Wedding in 2025. By Kat Dadswell Make the most of the last few moments of your big day with an epic closing    
number. Here's our take on the best last dance songs for your wedding in 2025.

[100 Best Wedding Songs For Every Moment Of Your Special Day](https://dallasoasis.com/best-wedding-songs/)
10. Wedding Exit Songs. The wedding exit is your grand finale. It's the moment when you leave the reception as a married couple, heading off
to start your new life together. The music for your exit should be upbeat, joyful, and full of excitement. This is your chance to celebrate 
the end of an incredible day and the beginning of your future ...

[Wedding Song Finder: Wedding Music for Every Moment - Bands For Hire](https://www.bandsforhire.net/blog/wedding-songs)
Our database has been curated by the experienced staff at Bands For Hire and features a huge selection of music to cover the bridal
entrance, signing of the registers, recessional, drinks reception, first dance, and more. So, whether you're searching for romantic ceremony
music or a classic end-of-the-night sing-along, you're in the right place.

Out: None
[Step 0: Duration 23.05 seconds| Input tokens: 2,080 | Output tokens: 69]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  # List of popular wedding songs categorized by different moments                                                                          
                                                                                                                                            
  # Ceremony Songs                                                                                                                          
  ceremony_songs = [                                                                                                                        
      "Here Comes the Sun - The Beatles",                                                                                                   
      "Canon in D - Pachelbel",                                                                                                             
      "A Thousand Years - Christina Perri",                                                                                                 
      "You Are the Best Thing - Ray LaMontagne",                                                                                            
      "I Do - Beyoncé",                                                                                                                     
      "I Will Always Love You - Whitney Houston",                                                                                           
      "Our Song - Taylor Swift",                                                                                                            
      "Marry You - Bruno Mars",                                                                                                             
      "Your Song - Elton John",                                                                                                             
      "At Last - Etta James"                                                                                                                
  ]                                                                                                                                         
                                                                                                                                            
  # Entrance Songs                                                                                                                          
  entrance_songs = [                                                                                                                        
      "Walking Down the aisle - Alison Krauss",                                                                                             
      "Here Comes the Bride - Andra Day",                                                                                                   
      "Bridal Chime - Various Artists",                                                                                                     
      "Here Comes the Bride - The Divine Comedy",                                                                                           
      "Here Comes the Bride - Beyoncé",                                                                                                     
      "Here Comes the Bride - Alison Krauss",                                                                                               
      "Here Comes the Bride - Patti Austin",                                                                                                
      "Here Comes the Bride - Sarah McLachlan",                                                                                             
      "Here Comes the Bride - The Divine Comedy",                                                                                           
      "Here Comes the Bride - Andrea Andrea"                                                                                                
  ]                                                                                                                                         
                                                                                                                                            
  # First Dance Songs                                                                                                                       
  first_dance_songs = [                                                                                                                     
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "All of Me - John Legend",                                                                                                            
      "Love Story - Taylor Swift",                                                                                                          
      "I Do - Beyoncé",                                                                                                                     
      "Love Me Again - John Newman",                                                                                                        
      "When We Were Young - Adele",                                                                                                         
      "I Will Always Love You - Whitney Houston",                                                                                           
      "Your Song - Elton John",                                                                                                             
      "You Are the Best Thing - Ray LaMontagne",                                                                                            
      "A Thousand Years - Christina Perri"                                                                                                  
  ]                                                                                                                                         
                                                                                                                                            
  # Dance Floor Songs                                                                                                                       
  dance_floor_songs = [                                                                                                                     
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift",                                                                                                        
      "Like a Prayer - Madonna",                                                                                                            
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shape of You - Ed Sheeran",                                                                                                          
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Shake It Off - Taylor Swift",                                                                                                        
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Shake It Off - Taylor Swift"                                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Exit Songs                                                                                                                              
  exit_songs = [                                                                                                                            
      "Here's to Us - Kelly Clarkson",                                                                                                      
      "A Thousand Years - Christina Perri",                                                                                                 
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift",                                                                                                        
      "Shape of You - Ed Sheeran",                                                                                                          
      "Here's to Us - Kelly Clarkson",                                                                                                      
      "A Thousand Years - Christina Perri",                                                                                                 
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Uptown Funk - Mark Ronson ft. Bruno Mars"                                                                                            
  ]                                                                                                                                         
                                                                                                                                            
  # Compile the recommendations                                                                                                             
  wedding_music_recommendations = {                                                                                                         
      "Ceremony Songs": ceremony_songs,                                                                                                     
      "Entrance Songs": entrance_songs,                                                                                                     
      "First Dance Songs": first_dance_songs,                                                                                               
      "Dance Floor Songs": dance_floor_songs,                                                                                               
      "Exit Songs": exit_songs                                                                                                              
  }                                                                                                                                         
                                                                                                                                            
  # Print the recommendations                                                                                                               
  print(wedding_music_recommendations)                                                                                                      
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
{'Ceremony Songs': ['Here Comes the Sun - The Beatles', 'Canon in D - Pachelbel', 'A Thousand Years - Christina Perri', 'You Are the Best   
Thing - Ray LaMontagne', 'I Do - Beyoncé', 'I Will Always Love You - Whitney Houston', 'Our Song - Taylor Swift', 'Marry You - Bruno Mars', 
'Your Song - Elton John', 'At Last - Etta James'], 'Entrance Songs': ['Walking Down the aisle - Alison Krauss', 'Here Comes the Bride -     
Andra Day', 'Bridal Chime - Various Artists', 'Here Comes the Bride - The Divine Comedy', 'Here Comes the Bride - Beyoncé', 'Here Comes the 
Bride - Alison Krauss', 'Here Comes the Bride - Patti Austin', 'Here Comes the Bride - Sarah McLachlan', 'Here Comes the Bride - The Divine 
Comedy', 'Here Comes the Bride - Andrea Andrea'], 'First Dance Songs': ["Can't Stop the Feeling! - Justin Timberlake", 'All of Me - John    
Legend', 'Love Story - Taylor Swift', 'I Do - Beyoncé', 'Love Me Again - John Newman', 'When We Were Young - Adele', 'I Will Always Love You
- Whitney Houston', 'Your Song - Elton John', 'You Are the Best Thing - Ray LaMontagne', 'A Thousand Years - Christina Perri'], 'Dance Floor
Songs': ['Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor Swift', 'Like a Prayer - Madonna', 'Uptown Funk - Mark Ronson   
ft. Bruno Mars', 'Shape of You - Ed Sheeran', "Can't Stop the Feeling! - Justin Timberlake", 'Shake It Off - Taylor Swift', 'Uptown Funk -  
Mark Ronson ft. Bruno Mars', "Can't Stop the Feeling! - Justin Timberlake", 'Shake It Off - Taylor Swift'], 'Exit Songs': ["Here's to Us -  
Kelly Clarkson", 'A Thousand Years - Christina Perri', "Can't Stop the Feeling! - Justin Timberlake", 'Uptown Funk - Mark Ronson ft. Bruno  
Mars', 'Shake It Off - Taylor Swift', 'Shape of You - Ed Sheeran', "Here's to Us - Kelly Clarkson", 'A Thousand Years - Christina Perri',   
"Can't Stop the Feeling! - Justin Timberlake", 'Uptown Funk - Mark Ronson ft. Bruno Mars']}

Out: None
[Step 1: Duration 37.08 seconds| Input tokens: 5,337 | Output tokens: 810]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 3 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  # Concise summary of the best wedding music recommendations                                                                               
                                                                                                                                            
  # Ceremony Songs                                                                                                                          
  ceremony_songs_summary = [                                                                                                                
      "Here Comes the Sun - The Beatles",                                                                                                   
      "Canon in D - Pachelbel",                                                                                                             
      "A Thousand Years - Christina Perri",                                                                                                 
      "You Are the Best Thing - Ray LaMontagne",                                                                                            
      "I Do - Beyoncé"                                                                                                                      
  ]                                                                                                                                         
                                                                                                                                            
  # Entrance Songs                                                                                                                          
  entrance_songs_summary = [                                                                                                                
      "Walking Down the aisle - Alison Krauss",                                                                                             
      "Here Comes the Bride - Andra Day",                                                                                                   
      "Bridal Chime - Various Artists",                                                                                                     
      "Here Comes the Bride - The Divine Comedy",                                                                                           
      "Here Comes the Bride - Beyoncé"                                                                                                      
  ]                                                                                                                                         
                                                                                                                                            
  # First Dance Songs                                                                                                                       
  first_dance_songs_summary = [                                                                                                             
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "All of Me - John Legend",                                                                                                            
      "Love Story - Taylor Swift",                                                                                                          
      "I Do - Beyoncé",                                                                                                                     
      "Love Me Again - John Newman"                                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Dance Floor Songs                                                                                                                       
  dance_floor_songs_summary = [                                                                                                             
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift",                                                                                                        
      "Like a Prayer - Madonna",                                                                                                            
      "Shape of You - Ed Sheeran",                                                                                                          
      "Can't Stop the Feeling! - Justin Timberlake"                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Exit Songs                                                                                                                              
  exit_songs_summary = [                                                                                                                    
      "Here's to Us - Kelly Clarkson",                                                                                                      
      "A Thousand Years - Christina Perri",                                                                                                 
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift"                                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Compile the concise recommendations                                                                                                     
  concise_wedding_music_recommendations = {                                                                                                 
      "Ceremony Songs": ceremony_songs_summary,                                                                                             
      "Entrance Songs": entrance_songs_summary,                                                                                             
      "First Dance Songs": first_dance_songs_summary,                                                                                       
      "Dance Floor Songs": dance_floor_songs_summary,                                                                                       
      "Exit Songs": exit_songs_summary                                                                                                      
  }                                                                                                                                         
                                                                                                                                            
  # Print the concise recommendations                                                                                                       
  print(concise_wedding_music_recommendations)                                                                                              
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
{'Ceremony Songs': ['Here Comes the Sun - The Beatles', 'Canon in D - Pachelbel', 'A Thousand Years - Christina Perri', 'You Are the Best   
Thing - Ray LaMontagne', 'I Do - Beyoncé'], 'Entrance Songs': ['Walking Down the aisle - Alison Krauss', 'Here Comes the Bride - Andra Day',
'Bridal Chime - Various Artists', 'Here Comes the Bride - The Divine Comedy', 'Here Comes the Bride - Beyoncé'], 'First Dance Songs':       
["Can't Stop the Feeling! - Justin Timberlake", 'All of Me - John Legend', 'Love Story - Taylor Swift', 'I Do - Beyoncé', 'Love Me Again -  
John Newman'], 'Dance Floor Songs': ['Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor Swift', 'Like a Prayer - Madonna',  
'Shape of You - Ed Sheeran', "Can't Stop the Feeling! - Justin Timberlake"], 'Exit Songs': ["Here's to Us - Kelly Clarkson", 'A Thousand    
Years - Christina Perri', "Can't Stop the Feeling! - Justin Timberlake", 'Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor 
Swift']}

Out: None
[Step 2: Duration 30.02 seconds| Input tokens: 10,736 | Output tokens: 1,298]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 4 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  # Corrected concise summary of the best wedding music recommendations                                                                     
                                                                                                                                            
  # Ceremony Songs                                                                                                                          
  ceremony_songs_summary = [                                                                                                                
      "Here Comes the Sun - The Beatles",                                                                                                   
      "Canon in D - Pachelbel",                                                                                                             
      "A Thousand Years - Christina Perri",                                                                                                 
      "You Are the Best Thing - Ray LaMontagne",                                                                                            
      "I Do - Beyoncé"                                                                                                                      
  ]                                                                                                                                         
                                                                                                                                            
  # Entrance Songs                                                                                                                          
  entrance_songs_summary = [                                                                                                                
      "Walking Down the Aisle - Alison Krauss",                                                                                             
      "Here Comes the Bride - Andra Day",                                                                                                   
      "Bridal Chime - Various Artists",                                                                                                     
      "Here Comes the Bride - The Divine Comedy",                                                                                           
      "Here Comes the Bride - Beyoncé"                                                                                                      
  ]                                                                                                                                         
                                                                                                                                            
  # First Dance Songs                                                                                                                       
  first_dance_songs_summary = [                                                                                                             
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "All of Me - John Legend",                                                                                                            
      "Love Story - Taylor Swift",                                                                                                          
      "I Do - Beyoncé",                                                                                                                     
      "Love Me Again - John Newman"                                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Dance Floor Songs                                                                                                                       
  dance_floor_songs_summary = [                                                                                                             
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift",                                                                                                        
      "Like a Prayer - Madonna",                                                                                                            
      "Shape of You - Ed Sheeran",                                                                                                          
      "Can't Stop the Feeling! - Justin Timberlake"                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Exit Songs                                                                                                                              
  exit_songs_summary = [                                                                                                                    
      "Here's to Us - Kelly Clarkson",                                                                                                      
      "A Thousand Years - Christina Perri",                                                                                                 
      "Can't Stop the Feeling! - Justin Timberlake",                                                                                        
      "Uptown Funk - Mark Ronson ft. Bruno Mars",                                                                                           
      "Shake It Off - Taylor Swift"                                                                                                         
  ]                                                                                                                                         
                                                                                                                                            
  # Compile the corrected concise recommendations                                                                                           
  corrected_concise_wedding_music_recommendations = {                                                                                       
      "Ceremony Songs": ceremony_songs_summary,                                                                                             
      "Entrance Songs": entrance_songs_summary,                                                                                             
      "First Dance Songs": first_dance_songs_summary,                                                                                       
      "Dance Floor Songs": dance_floor_songs_summary,                                                                                       
      "Exit Songs": exit_songs_summary                                                                                                      
  }                                                                                                                                         
                                                                                                                                            
  # Print the corrected concise recommendations                                                                                             
  print(corrected_concise_wedding_music_recommendations)                                                                                    
                                                                                                                                            
  # Provide the final answer                                                                                                                
  final_answer(corrected_concise_wedding_music_recommendations)                                                                             
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
{'Ceremony Songs': ['Here Comes the Sun - The Beatles', 'Canon in D - Pachelbel', 'A Thousand Years - Christina Perri', 'You Are the Best   
Thing - Ray LaMontagne', 'I Do - Beyoncé'], 'Entrance Songs': ['Walking Down the Aisle - Alison Krauss', 'Here Comes the Bride - Andra Day',
'Bridal Chime - Various Artists', 'Here Comes the Bride - The Divine Comedy', 'Here Comes the Bride - Beyoncé'], 'First Dance Songs':       
["Can't Stop the Feeling! - Justin Timberlake", 'All of Me - John Legend', 'Love Story - Taylor Swift', 'I Do - Beyoncé', 'Love Me Again -  
John Newman'], 'Dance Floor Songs': ['Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor Swift', 'Like a Prayer - Madonna',  
'Shape of You - Ed Sheeran', "Can't Stop the Feeling! - Justin Timberlake"], 'Exit Songs': ["Here's to Us - Kelly Clarkson", 'A Thousand    
Years - Christina Perri', "Can't Stop the Feeling! - Justin Timberlake", 'Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor 
Swift']}

Out - Final answer: {'Ceremony Songs': ['Here Comes the Sun - The Beatles', 'Canon in D - Pachelbel', 'A Thousand Years - Christina Perri', 
'You Are the Best Thing - Ray LaMontagne', 'I Do - Beyoncé'], 'Entrance Songs': ['Walking Down the Aisle - Alison Krauss', 'Here Comes the  
Bride - Andra Day', 'Bridal Chime - Various Artists', 'Here Comes the Bride - The Divine Comedy', 'Here Comes the Bride - Beyoncé'], 'First 
Dance Songs': ["Can't Stop the Feeling! - Justin Timberlake", 'All of Me - John Legend', 'Love Story - Taylor Swift', 'I Do - Beyoncé',     
'Love Me Again - John Newman'], 'Dance Floor Songs': ['Uptown Funk - Mark Ronson ft. Bruno Mars', 'Shake It Off - Taylor Swift', 'Like a    
Prayer - Madonna', 'Shape of You - Ed Sheeran', "Can't Stop the Feeling! - Justin Timberlake"], 'Exit Songs': ["Here's to Us - Kelly        
Clarkson", 'A Thousand Years - Christina Perri', "Can't Stop the Feeling! - Justin Timberlake", 'Uptown Funk - Mark Ronson ft. Bruno Mars', 
'Shake It Off - Taylor Swift']}
[Step 3: Duration 27.79 seconds| Input tokens: 17,462 | Output tokens: 1,815]
```