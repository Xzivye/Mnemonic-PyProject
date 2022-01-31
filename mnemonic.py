#!/usr/bin/env python3
#Sofia Rosa
#November 25th 2021

# Menmonic generator for up to 7 words.
# Beware this script is rude.
# There's also geeky references atm such as D&D monsters because Y nouns...
# Structure: adjective adjective noun verb adjective adjective noun
# 7-ish of each letter for now?

import random
import time

#libraries nouns:
noun_a = ["Apples", "Apricots", "Avocados", "Alpacas", "Ants", "Alligators", "Anteaters"]
noun_b = ["Bananas", "Blueberries", "Berries", "Badgers", "Birds", "Beagles", "Bobcats", "Bears"]
noun_c = ["Cats", "Cardinals", "Coffee", "Camels", "Cheetahs", "Cherries", "Carrots", "Cakes", "Cheeses"]
noun_d = ["Dogs", "Dik-Diks", "Dolphins", "Dingos", "Dewberries", "Durians", "Dates"]
noun_e = ["Eclairs", "Eels", "Eggs", "Eggnogs", "Enchiladas", "Eagles", "Elephants"]
noun_f = ["Foxes", "Fishes", "Frogs", "Ferrets", "Falafels", "Figs", "Frankfurters"]
noun_g = ["Garlics", "Gooseberries", "Grapes", "Guavas", "Giraffes", "Geckos", "Gorillas"]
noun_h = ["Humans", "Horses", "Hamsters", "Hyenas", "Hamburgers", "Hashbrowns", "Haddocks"]
noun_i = ["Iguanas", "Impalas", "Ibexs", "Insects", "Illusionists", "Imps", "Icicles"]
noun_j = ["Jackals", "Jaguars", "Jackdaws", "Jellyfishes", "Jalapenos", "Jelly Beans", "Jams"]
noun_k = ["Koalas", "Kiwis", "Kangaroos", "Kudus", "Kittens", "Kobolds", "Kenkus", "Krakens"]
noun_l = ["Lions", "Leopards", "Lemurs", "Llamas", "Lemons", "Limes", "Lasagnas"]
noun_m = ["Magpies", "Moles", "Mice", "Macaroons", "Mushrooms", "Mangos", "Marshmallows"]
noun_n = ["Newts", "Nightingales", "Narwhals", "Nachos", "Nuts", "Nagas", "Nightwalkers", "Nilbogs"]
noun_o = ["Ocelots", "Octopuses", "Ostriches", "Otters", "Oatcakes", "Onions", "Omelets"]
noun_p = ["Pangolins", "Parrots", "Peacocks", "Penguins", "Pancakes", "Papayas", "Pastas", "Panthers"]
noun_q = ["Quails", "Quokkas", "Quolls", "Quesadillas", "Quiches", "Quicklings", "Quarterbacks", "Queens"]
noun_r = ["Raccoons", "Robins", "Rhinos", "Raspberries", "Ramen", "Raisins", "Reptiles"]
noun_s = ["Salmons", "Seals", "Sharks", "Sloths", "Sausages", "Salads", "Soups"]
noun_t = ["Turtles", "Tigers", "Tapirs", "Toucans", "Tomatoes", "Tarts", "Tofu"]
noun_u = ["UFOs", "Uakaris", "Umbrellabirds", "Utonagans", "Unicorns", "Umbraxakars"]
noun_v = ["Vampires", "Valenar", "Vultures", "Veal", "Vegetables", "Venison"]
noun_w = ["Warthogs", "Wombats", "Walruses", "Wildebeest", "Wolves", "Wasabi", "Walnuts"]
noun_x = ["X-men", "Xenurines", "Xiphias", "Xylophones", "Xiphias", "Xiaosaurus", "Xenops"]
noun_y = ["Yaks", "Yoghurts", "Yams", "Yetis", "Yugoloths", "Yuan-tis", "Yumyulacks", "You"]
noun_z = ["Zombies", "Zebras", "Zucchinis", "Zealots", "Zebrafishes", "Zepplins", "Zookeepers"]

#library verbs
verb_a = ["Adore", "Assemble", "Accelerate", "Acquire", "Authorize"]
verb_b = ["Balanced", "Built", "Blow", "Burn", "Bend", "Balance"]
verb_c = ["Call", "Cook", "Copy", "Cure", "Capture", "Craft"]
verb_d = ["Draw", "Drop", "Dare", "Deny", "Drag", "Define", "Discover"]
verb_e = ["Edit", "Echo", "Educate", "Enable", "Encourage", "Export"]
verb_f = ["Find", "Face", "Fail", "Flee", "Fire", "Forge"]
verb_g = ["Give", "Grab", "Generate", "Guide", "Govern"]
verb_h = ["Have", "Hold", "Help", "Hurt", "Hate"]
verb_i = ["Illustrate", "Imagine", "Improve", "Import", "Influence", "Inspire"]
verb_j = ["Join", "Judge", "Justified"]
verb_k = ["Know", "Kill", "Knit"]
verb_l = ["Like", "Love", "Lead", "Lose", "Lift", "Lecture", "Locate"]
verb_m = ["Move", "Make", "Meet", "Miss", "Maintain", "Mentor", "Monitor", "Motivate"]
verb_n = ["Need", "Name", "Navigate", "Nominate"]
verb_o = ["Obey", "Observe", "Offer", "Operate", "Organise", "Orientate"]
verb_p = ["Purchase", "Pick", "Pass", "Plan", "Prepare", "Persuade"]
verb_q = ["Qualify", "Quantify", "Question", "Quote"]
verb_r = ["Roll", "Rule", "Ring", "Rate", "Recognise", "Refer", "Recruit"]
verb_s = ["Show", "Save", "Seek", "Stop", "Satisfy", "Sold", "Supply"]
verb_t = ["Turn", "Take", "Test", "Target", "Teach", "Translate"]
verb_u = ["Urge", "Unify", "Update", "Use", "Unite"]
verb_v = ["Verify", "Verbalise", "Validate"]
verb_w = ["Want", "Watch", "Warn", "Wear", "Win", "Write", "Warn"]
verb_x = ["X-ray", "Xerox", "Xenograft", "Xylograph"]
verb_y = ["Yelp", "Yang", "Yowl", "Yip", "Yearn"]
verb_z = ["Zoom", "Zip", "Zone", "Zigzag", "Zap"]

#library adjectives
adjective_a = ["Adorable", "Amusing", "Annoying", "Awful", "Alert", "Angry", "Anxious", "Aggressive", "Arrogant"]
adjective_b = ["Blue", "Bad", "Beautiful", "Black", "Bored", "Bright", "Busy", "Brave", "Bold", "Bald"]
adjective_c = ["Cute", "Calm", "Charming", "Careful", "Cheerful", "Clever", "Clean", "Cautious", "Clumsy", " Colourful", "Confused", "Creepy"]
adjective_d = ["Dark", "Depressed", "Determined", "Dizzy", "Dull", "Distinct", "Different", "Delightful", "Dead", "Defiant", "Dangerous"]
adjective_e = ["Eager", "Easy", "Elegant", "Embarrassed", "Enchanting", "Enthusiastic", "Excited", "Evil", "Expensive", "Energetic"]
adjective_f = ["Fluffy", "Fair", "Fancy", "Fierce", "Fantastic", "Fine", "Foolish", "Fragile", "Frantic", "Friendly", "Funny"]
adjective_g = ["Green", "Good", "Gifted", "Glamorous", "Gentle", "Glorious", "Graceful", "Grumpy", "Grotesque"]
adjective_h = ["Healthy", "Helpful", "Hungry", "Helpless", "Hilarious", "Homeless", "Homely", "Horrible"]
adjective_i = ["Ill", "Important", "Impossible", "Innocent", "Inquisitive", "Itchy", "Introverted", "Idle", "Improbable"]
adjective_j = ["Jealous", "Jittery", "Jolly", "Joyous", "Jovial", "Jesting", "Jinxed", "Jarring"]
adjective_k = ["Kind", "Keen", "Knowledgeable", "Kingly", "Kitschy", "Knitted", "Knotty", "Kooky"]
adjective_l = ["Lazy", "Light", "Lively", "Lonely", "Long", "Lovely", "Lucky", "Lanky"]
adjective_m = ["Magnificent", "Modern", "Muddy", "Mushy", "Mysterious", "Maniacle", "Mean", "Magical"]
adjective_n = ["Nasty", "Nice", "Naughty", "Nervous", "Nutty", "Native", "Needy", "New"]
adjective_o = ["Orange", "Obedient", "Obnoxious", "Odd", "Outrageous", "Outstanding", "Open"]
adjective_p = ["Panicky", "Perfect", "Plain", "Pleasant", "Poisoned", "Poor", "Powerful", "Proud", "Prickly", "Puzzled", "Putrid"]
adjective_q = ["Quaint", "Quick", "Quirky", "Questioning", "Quelled"]
adjective_r = ["Real", "Relieved", "Repulsive", "Rich", "Rustic", "Roasted", "Realistic", "Rhyming"]
adjective_s = ["Shy", "Silly", "Selfish", "Shiny", "Scary", "Sleepy", "Smiling", "Sparkling", "Strange", "Super"]
adjective_t = ["Talented", "Tame", "Tasty", "Tender", "Tense", "Terrible", "Thoughtful", "Tired", "Tough", "Troubled"]
adjective_u = ["Ugly", "Unusual", "Upset", "Uptight", "Unsightly", "Uninterested", "Useful"]
adjective_v = ["Violet", "Vast", "Victorious", "Vivacious", "Verbal", "Void", "Vicarious", "Virtual"]
adjective_w = ["Wandering", "Weary", "Wicked", "Wild", "Witty", "Worried", "Wrong", "Wacky"]
adjective_x = ["Xenophobic", "Xenogenic", "Xenotropic", "Xylographic", "Xyloid"]
adjective_y = ["Yawning", "Yielding", "Yeasty", "Yucky", "Young", "Youthful"]
adjective_z = ["Zany", "Zealous", "Zestful", "Zippy", "Zonal"]


# 1- really? 2 - do you even need a mnemonic for this? 3-noun verb noun / 4-noun verb adjective noun / 5-adjective noun verb adjective noun
# anything else - I dont know what you put in here but those are certainly not letters


while True:
    user_letters = input("Please input up to 7 letters for your mnemonic.\n").lower()

#if the user cant read

    if len(user_letters) > 7:
        print ("We are not able to generate mnemonics this long at the current time. Please try again");
        continue

    if user_letters.isdigit():
        print ("I think you need to go back to kindergarten...");
        continue
        
    if user_letters.isalpha() == True:

    #1 letter. dont foget to mock them
        if len(user_letters) == 1:
            print ("Really?");
            continue

    # 2 letters
        elif len(user_letters) == 2:
            print ("You really need a mnemonic for 2 words? Come on, make an effort.");
            continue

    #3 letters
        elif len(user_letters) == 3:
        #noun_0
            if "a" in user_letters:
                output_0 = random.choice(noun_a)
                noun_a.remove(output_0);
        
                
            elif "b" in user_letters:
                output_0 = random.choice(noun_b)
                noun_b.remove(output_0);

            elif "c" in user_letters:
                output_0 = random.choice(noun_c)
                noun_c.remove(output_0);

            elif "d" in user_letters:
                output_0 = random.choice(noun_d)
                noun_d.remove(output_0);

            elif "e" in user_letters:
                output_0 = random.choice(noun_e)
                noun_e.remove(output_0);

            elif "f" in user_letters:
                output_0 = random.choice(noun_f)
                noun_f.remove(output_0);

            elif "g" in user_letters:
                output_0 = random.choice(noun_g)
                noun_g.remove(output_0);

            elif "h" in user_letters:
                output_0 = random.choice(noun_h)
                noun_h.remove(output_0);

            elif "i" in user_letters:
                output_0 = random.choice(noun_i)
                noun_i.remove(output_0);    

            elif "j" in user_letters:
                output_0 = random.choice(noun_j)
                noun_j.remove(output_0);

            elif "k" in user_letters:
                output_0 = random.choice(noun_k)
                noun_k.remove(output_0);

            elif "l" in user_letters:
                output_0 = random.choice(noun_l)
                noun_l.remove(output_0);

            elif "m" in user_letters:
                output_0 = random.choice(noun_m)
                noun_m.remove(output_0);         

            elif "n" in user_letters:
                output_0 = random.choice(noun_n)
                noun_n.remove(output_0);

            elif "o" in user_letters:
                output_0 = random.choice(noun_o)
                noun_o.remove(output_0);

            elif "p" in user_letters:
                output_0 = random.choice(noun_p)
                noun_p.remove(output_0);   

            elif "q" in user_letters:
                output_0 = random.choice(noun_q)
                noun_q.remove(output_0);   

            elif "r" in user_letters:
                output_0 = random.choice(noun_r)
                noun_r.remove(output_0);   

            elif "s" in user_letters:
                output_0 = random.choice(noun_s)
                noun_s.remove(output_0);   

            elif "t" in user_letters:
                output_0 = random.choice(noun_t)
                noun_t.remove(output_0);   

            elif "u" in user_letters:
                output_0 = random.choice(noun_u)
                noun_u.remove(output_0);   

            elif "v" in user_letters:
                output_0 = random.choice(noun_v)
                noun_v.remove(output_0);   

            elif "w" in user_letters:
                output_0 = random.choice(noun_w)
                noun_w.remove(output_0);   

            elif "x" in user_letters:
                output_0 = random.choice(noun_x)
                noun_x.remove(output_0);   

            elif "y" in user_letters:
                output_0 = random.choice(noun_y)
                noun_y.remove(output_0);   

            elif "z" in user_letters:
                output_0 = random.choice(noun_z)
                noun_z.remove(output_0);
        #code verb_1
            if user_letters[1] == "a":
                output_1 = random.choice(verb_a);
                    
            elif user_letters[1] == "b":
                output_1 = random.choice(verb_b);
                    
            elif user_letters[1] == "c":
                output_1 = random.choice(verb_c);

            elif user_letters[1] == "d":
                output_1 = random.choice(verb_d);

            elif user_letters[1] == "e":
                output_1 = random.choice(verb_e);

            elif user_letters[1] == "f":
                output_1 = random.choice(verb_f);

            elif user_letters[1] == "g":
                output_1 = random.choice(verb_g);

            elif user_letters[1] == "h":
                output_1 = random.choice(verb_h);

            elif user_letters[1] == "i":
                output_1 = random.choice(verb_i);

            elif user_letters[1] == "j":
                output_1 = random.choice(verb_j);

            elif user_letters[1] == "k":
                output_1 = random.choice(verb_k);

            elif user_letters[1] == "l":
                output_1 = random.choice(verb_l);

            elif user_letters[1] == "m":
                output_1 = random.choice(verb_m);       

            elif user_letters[1] == "n":
                output_1 = random.choice(verb_n);

            elif user_letters[1] == "o":
                output_1 = random.choice(verb_o);    

            elif user_letters[1] == "p":
                output_1 = random.choice(verb_p);

            elif user_letters[1] == "q":
                output_1 = random.choice(verb_q);

            elif user_letters[1] == "r":
                output_1 = random.choice(verb_r);

            elif user_letters[1] == "s":
                output_1 = random.choice(verb_s);

            elif user_letters[1] == "t":
                output_1 = random.choice(verb_t);

            elif user_letters[1] == "u":
                output_1 = random.choice(verb_u);

            elif user_letters[1] == "v":
                output_1 = random.choice(verb_v);

            elif user_letters[1] == "w":
                output_1 = random.choice(verb_w);

            elif user_letters[1] == "x":
                output_1 = random.choice(verb_x);

            elif user_letters[1] == "y":
                output_1 = random.choice(verb_y);

            elif user_letters[1] == "z":
                output_1 = random.choice(verb_z);    
        #noun_2
            if "a" in user_letters:
                output_2 = random.choice(noun_a);
                
            elif "b" in user_letters:
                output_2 = random.choice(noun_b);

            elif "c" in user_letters:
                output_2 = random.choice(noun_c);

            elif "d" in user_letters:
                output_2 = random.choice(noun_d);

            elif "e" in user_letters:
                output_2 = random.choice(noun_e);

            elif "f" in user_letters:
                output_2 = random.choice(noun_f);

            elif "g" in user_letters:
                output_2 = random.choice(noun_g);

            elif "h" in user_letters:
                output_2 = random.choice(noun_h);

            elif "i" in user_letters:
                output_2 = random.choice(noun_i);

            elif "j" in user_letters:
                output_2 = random.choice(noun_j);

            elif "k" in user_letters:
                output_2 = random.choice(noun_k);

            elif "l" in user_letters:
                output_2 = random.choice(noun_l);

            elif "m" in user_letters:
                output_2 = random.choice(noun_m);         

            elif "n" in user_letters:
                output_2 = random.choice(noun_n);

            elif "o" in user_letters:
                output_2 = random.choice(noun_o);

            elif "p" in user_letters:
                output_2 = random.choice(noun_p);   

            elif "q" in user_letters:
                output_2 = random.choice(noun_q);   

            elif "r" in user_letters:
                output_2 = random.choice(noun_r);   

            elif "s" in user_letters:
                output_2 = random.choice(noun_s);   

            elif "t" in user_letters:
                output_2 = random.choice(noun_t);   

            elif "u" in user_letters:
                output_2 = random.choice(noun_u);   

            elif "v" in user_letters:
                output_2 = random.choice(noun_v);   

            elif "w" in user_letters:
                output_2 = random.choice(noun_w);   

            elif "x" in user_letters:
                output_2 = random.choice(noun_x);   

            elif "y" in user_letters:
                output_2 = random.choice(noun_y);   

            elif "z" in user_letters:
                output_2 = random.choice(noun_z);
        #print   
            print (output_0, output_1, output_2);
            break

    #4 letters
        elif len(user_letters) == 4:
        #noun_0
            if "a" in user_letters:
                output_0 = random.choice(noun_a)
                noun_a.remove(output_0);
                
            elif "b" in user_letters:
                output_0 = random.choice(noun_b)
                noun_b.remove(output_0);

            elif "c" in user_letters:
                output_0 = random.choice(noun_c)
                noun_c.remove(output_0);

            elif "d" in user_letters:
                output_0 = random.choice(noun_d)
                noun_d.remove(output_0);

            elif "e" in user_letters:
                output_0 = random.choice(noun_e)
                noun_e.remove(output_0);

            elif "f" in user_letters:
                output_0 = random.choice(noun_f)
                noun_f.remove(output_0);

            elif "g" in user_letters:
                output_0 = random.choice(noun_g)
                noun_g.remove(output_0);

            elif "h" in user_letters:
                output_0 = random.choice(noun_h)
                noun_h.remove(output_0);

            elif "i" in user_letters:
                output_0 = random.choice(noun_i)
                noun_i.remove(output_0);

            elif "j" in user_letters:
                output_0 = random.choice(noun_j)
                noun_j.remove(output_0);

            elif "k" in user_letters:
                output_0 = random.choice(noun_k)
                noun_k.remove(output_0);

            elif "l" in user_letters:
                output_0 = random.choice(noun_l)
                noun_l.remove(output_0);

            elif "m" in user_letters:
                output_0 = random.choice(noun_m)
                noun_m.remove(output_0);         

            elif "n" in user_letters:
                output_0 = random.choice(noun_n)
                noun_n.remove(output_0);

            elif "o" in user_letters:
                output_0 = random.choice(noun_o)
                noun_o.remove(output_0);

            elif "p" in user_letters:
                output_0 = random.choice(noun_p)
                noun_p.remove(output_0);   

            elif "q" in user_letters:
                output_0 = random.choice(noun_q)
                noun_q.remove(output_0);   

            elif "r" in user_letters:
                output_0 = random.choice(noun_r)
                noun_r.remove(output_0);   

            elif "s" in user_letters:
                output_0 = random.choice(noun_s)
                noun_s.remove(output_0);   

            elif "t" in user_letters:
                output_0 = random.choice(noun_t)
                noun_t.remove(output_0);   

            elif "u" in user_letters:
                output_0 = random.choice(noun_u)
                noun_u.remove(output_0);   

            elif "v" in user_letters:
                output_0 = random.choice(noun_v)
                noun_v.remove(output_0);   

            elif "w" in user_letters:
                output_0 = random.choice(noun_w)
                noun_w.remove(output_0);   

            elif "x" in user_letters:
                output_0 = random.choice(noun_x)
                noun_x.remove(output_0);   

            elif "y" in user_letters:
                output_0 = random.choice(noun_y)
                noun_y.remove(output_0);   

            elif "z" in user_letters:
                output_0 = random.choice(noun_z)
                noun_z.remove(output_0);
        #verb_1
            if user_letters[1] == "a":
                output_1 = random.choice(verb_a);
                    
            elif user_letters[1] == "b":
                output_1 = random.choice(verb_b);
                    
            elif user_letters[1] == "c":
                output_1 = random.choice(verb_c);

            elif user_letters[1] == "d":
                output_1 = random.choice(verb_d);

            elif user_letters[1] == "e":
                output_1 = random.choice(verb_e);

            elif user_letters[1] == "f":
                output_1 = random.choice(verb_f);

            elif user_letters[1] == "g":
                output_1 = random.choice(verb_g);

            elif user_letters[1] == "h":
                output_1 = random.choice(verb_h);

            elif user_letters[1] == "i":
                output_1 = random.choice(verb_i);

            elif user_letters[1] == "j":
                output_1 = random.choice(verb_j);

            elif user_letters[1] == "k":
                output_1 = random.choice(verb_k);

            elif user_letters[1] == "l":
                output_1 = random.choice(verb_l);

            elif user_letters[1] == "m":
                output_1 = random.choice(verb_m);       

            elif user_letters[1] == "n":
                output_1 = random.choice(verb_n);

            elif user_letters[1] == "o":
                output_1 = random.choice(verb_o);    

            elif user_letters[1] == "p":
                output_1 = random.choice(verb_p);

            elif user_letters[1] == "q":
                output_1 = random.choice(verb_q);

            elif user_letters[1] == "r":
                output_1 = random.choice(verb_r);

            elif user_letters[1] == "s":
                output_1 = random.choice(verb_s);

            elif user_letters[1] == "t":
                output_1 = random.choice(verb_t);

            elif user_letters[1] == "u":
                output_1 = random.choice(verb_u);

            elif user_letters[1] == "v":
                output_1 = random.choice(verb_v);

            elif user_letters[1] == "w":
                output_1 = random.choice(verb_w);

            elif user_letters[1] == "x":
                output_1 = random.choice(verb_x);

            elif user_letters[1] == "y":
                output_1 = random.choice(verb_y);

            elif user_letters[1] == "z":
                output_1 = random.choice(verb_z);    
        #adjective_2    
            if user_letters[2] == "a":
                output_2 = random.choice(adjective_a);
                    
            elif user_letters[2] == "b":
                output_2 = random.choice(adjective_b);
                    
            elif user_letters[2] == "c":
                output_2 = random.choice(adjective_c);

            elif user_letters[2] == "d":
                output_2 = random.choice(adjective_d);

            elif user_letters[2] == "e":
                output_2 = random.choice(adjective_e);

            elif user_letters[2] == "f":
                output_2 = random.choice(adjective_f);

            elif user_letters[2] == "g":
                output_2 = random.choice(adjective_g);

            elif user_letters[2] == "h":
                output_2 = random.choice(adjective_h);

            elif user_letters[2] == "i":
                output_2 = random.choice(adjective_i);

            elif user_letters[2] == "j":
                output_2 = random.choice(adjective_j);

            elif user_letters[2] == "k":
                output_2 = random.choice(adjective_k);

            elif user_letters[2] == "l":
                output_2 = random.choice(adjective_l);

            elif user_letters[2] == "m":
                output_2 = random.choice(adjective_m);       

            elif user_letters[2] == "n":
                output_2 = random.choice(adjective_n);

            elif user_letters[2] == "o":
                output_2 = random.choice(adjective_o);    

            elif user_letters[2] == "p":
                output_2 = random.choice(adjective_p);

            elif user_letters[2] == "q":
                output_2 = random.choice(adjective_q);

            elif user_letters[2] == "r":
                output_2 = random.choice(adjective_r);

            elif user_letters[2] == "s":
                output_2 = random.choice(adjective_s);

            elif user_letters[2] == "t":
                output_2 = random.choice(adjective_t);

            elif user_letters[2] == "u":
                output_2 = random.choice(adjective_u);

            elif user_letters[2] == "v":
                output_2 = random.choice(adjective_v);

            elif user_letters[2] == "w":
                output_2 = random.choice(adjective_w);

            elif user_letters[2] == "x":
                output_2 = random.choice(adjective_x);

            elif user_letters[2] == "y":
                output_2 = random.choice(adjective_y);

            elif user_letters[2] == "z":
                output_2 = random.choice(adjective_z);        
        #noun_3
            if "a" in user_letters:
                output_3 = random.choice(noun_a);
                
            elif "b" in user_letters:
                output_3 = random.choice(noun_b);

            elif "c" in user_letters:
                output_3 = random.choice(noun_c);

            elif "d" in user_letters:
                output_3 = random.choice(noun_d);

            elif "e" in user_letters:
                output_3 = random.choice(noun_e);

            elif "f" in user_letters:
                output_3 = random.choice(noun_f);

            elif "g" in user_letters:
                output_3 = random.choice(noun_g);

            elif "h" in user_letters:
                output_3 = random.choice(noun_h);

            elif "i" in user_letters:
                output_3 = random.choice(noun_i);

            elif "j" in user_letters:
                output_3 = random.choice(noun_j);

            elif "k" in user_letters:
                output_3 = random.choice(noun_k);

            elif "l" in user_letters:
                output_3 = random.choice(noun_l);

            elif "m" in user_letters:
                output_3 = random.choice(noun_m);         

            elif "n" in user_letters:
                output_3 = random.choice(noun_n);

            elif "o" in user_letters:
                output_3 = random.choice(noun_o);

            elif "p" in user_letters:
                output_3 = random.choice(noun_p);   

            elif "q" in user_letters:
                output_3 = random.choice(noun_q);   

            elif "r" in user_letters:
                output_3 = random.choice(noun_r);   

            elif "s" in user_letters:
                output_3 = random.choice(noun_s);   

            elif "t" in user_letters:
                output_3 = random.choice(noun_t);   

            elif "u" in user_letters:
                output_3 = random.choice(noun_u);   

            elif "v" in user_letters:
                output_3 = random.choice(noun_v);   

            elif "w" in user_letters:
                output_3 = random.choice(noun_w);   

            elif "x" in user_letters:
                output_3 = random.choice(noun_x);   

            elif "y" in user_letters:
                output_3 = random.choice(noun_y);   

            elif "z" in user_letters:
                output_3 = random.choice(noun_z);
        #print
            print (output_0, output_1, output_2, output_3);
            break

    #5 letters
        elif len(user_letters) == 5:
        #adjective_0
            if user_letters[0] == "a":
                output_0 = random.choice(adjective_a)
                adjective_a.remove(output_0);
                    
            elif user_letters[0] == "b":
                output_0 = random.choice(adjective_b)
                adjective_b.remove(output_0);
                    
            elif user_letters[0] == "c":
                output_0 = random.choice(adjective_c)
                adjective_c.remove(output_0);

            elif user_letters[0] == "d":
                output_0 = random.choice(adjective_d)
                adjective_d.remove(output_0);

            elif user_letters[0] == "e":
                output_0 = random.choice(adjective_e)
                adjective_e.remove(output_0);

            elif user_letters[0] == "f":
                output_0 = random.choice(adjective_f)
                adjective_f.remove(output_0);

            elif user_letters[0] == "g":
                output_0 = random.choice(adjective_g)
                adjective_g.remove(output_0);

            elif user_letters[0] == "h":
                output_0 = random.choice(adjective_h)
                adjective_h.remove(output_0);

            elif user_letters[0] == "i":
                output_0 = random.choice(adjective_i)
                adjective_i.remove(output_0);

            elif user_letters[0] == "j":
                output_0 = random.choice(adjective_j)
                adjective_j.remove(output_0);

            elif user_letters[0] == "k":
                output_0 = random.choice(adjective_k)
                adjective_k.remove(output_0);

            elif user_letters[0] == "l":
                output_0 = random.choice(adjective_l)
                adjective_l.remove(output_0);

            elif user_letters[0] == "m":
                output_0 = random.choice(adjective_m)
                adjective_m.remove(output_0);       

            elif user_letters[0] == "n":
                output_0 = random.choice(adjective_n)
                adjective_n.remove(output_0);

            elif user_letters[0] == "o":
                output_0 = random.choice(adjective_o)
                adjective_o.remove(output_0);    

            elif user_letters[0] == "p":
                output_0 = random.choice(adjective_p)
                adjective_p.remove(output_0);

            elif user_letters[0] == "q":
                output_0 = random.choice(adjective_q)
                adjective_q.remove(output_0);

            elif user_letters[0] == "r":
                output_0 = random.choice(adjective_r)
                adjective_r.remove(output_0);

            elif user_letters[0] == "s":
                output_0 = random.choice(adjective_s)
                adjective_s.remove(output_0);

            elif user_letters[0] == "t":
                output_0 = random.choice(adjective_t)
                adjective_t.remove(output_0);

            elif user_letters[0] == "u":
                output_0 = random.choice(adjective_u)
                adjective_u.remove(output_0);

            elif user_letters[0] == "v":
                output_0 = random.choice(adjective_v)
                adjective_v.remove(output_0);

            elif user_letters[0] == "w":
                output_0 = random.choice(adjective_w)
                adjective_w.remove(output_0);

            elif user_letters[0] == "x":
                output_0 = random.choice(adjective_x)
                adjective_x.remove(output_0);

            elif user_letters[0] == "y":
                output_0 = random.choice(adjective_y)
                adjective_y.remove(output_0);

            elif user_letters[0] == "z":
                output_0 = random.choice(adjective_z)
                adjective_z.remove(output_0);
        #noun_1
            if "a" in user_letters:
                output_1 = random.choice(noun_a)
                noun_a.remove(output_1);
                
            elif "b" in user_letters:
                output_1 = random.choice(noun_b)
                noun_b.remove(output_1);

            elif "c" in user_letters:
                output_1 = random.choice(noun_c)
                noun_c.remove(output_1);

            elif "d" in user_letters:
                output_1 = random.choice(noun_d)
                noun_d.remove(output_1);

            elif "e" in user_letters:
                output_1 = random.choice(noun_e)
                noun_e.remove(output_1);

            elif "f" in user_letters:
                output_1 = random.choice(noun_f)
                noun_f.remove(output_1);

            elif "g" in user_letters:
                output_1 = random.choice(noun_g)
                noun_g.remove(output_1);

            elif "h" in user_letters:
                output_1 = random.choice(noun_h)
                noun_h.remove(output_1);

            elif "i" in user_letters:
                output_1 = random.choice(noun_i)
                noun_i.remove(output_1);

            elif "j" in user_letters:
                output_1 = random.choice(noun_j)
                noun_j.remove(output_1);

            elif "k" in user_letters:
                output_1 = random.choice(noun_k)
                noun_k.remove(output_1);

            elif "l" in user_letters:
                output_1 = random.choice(noun_l)
                noun_l.remove(output_1);

            elif "m" in user_letters:
                output_1 = random.choice(noun_m)
                noun_m.remove(output_1);         

            elif "n" in user_letters:
                output_1 = random.choice(noun_n)
                noun_n.remove(output_1);

            elif "o" in user_letters:
                output_1 = random.choice(noun_o)
                noun_o.remove(output_1);

            elif "p" in user_letters:
                output_1 = random.choice(noun_p)
                noun_p.remove(output_1);   

            elif "q" in user_letters:
                output_1 = random.choice(noun_q)
                noun_q.remove(output_1);   

            elif "r" in user_letters:
                output_1 = random.choice(noun_r)
                noun_r.remove(output_1);   

            elif "s" in user_letters:
                output_1 = random.choice(noun_s)
                noun_s.remove(output_1);   

            elif "t" in user_letters:
                output_1 = random.choice(noun_t)
                noun_t.remove(output_1);   

            elif "u" in user_letters:
                output_1 = random.choice(noun_u)
                noun_u.remove(output_1);   

            elif "v" in user_letters:
                output_1 = random.choice(noun_v)
                noun_v.remove(output_1);   

            elif "w" in user_letters:
                output_1 = random.choice(noun_w)
                noun_w.remove(output_1);   

            elif "x" in user_letters:
                output_1 = random.choice(noun_x)
                noun_x.remove(output_1);   

            elif "y" in user_letters:
                output_1 = random.choice(noun_y)
                noun_y.remove(output_1);   

            elif "z" in user_letters:
                output_1 = random.choice(noun_z)
                noun_z.remove(output_1);
        #verb_2
            if user_letters[2] == "a":
                output_2 = random.choice(verb_a);
                    
            elif user_letters[2] == "b":
                output_2 = random.choice(verb_b);
                    
            elif user_letters[2] == "c":
                output_2 = random.choice(verb_c);

            elif user_letters[2] == "d":
                output_2 = random.choice(verb_d);

            elif user_letters[2] == "e":
                output_2 = random.choice(verb_e);

            elif user_letters[2] == "f":
                output_2 = random.choice(verb_f);

            elif user_letters[2] == "g":
                output_2 = random.choice(verb_g);

            elif user_letters[2] == "h":
                output_2 = random.choice(verb_h);

            elif user_letters[2] == "i":
                output_2 = random.choice(verb_i);

            elif user_letters[2] == "j":
                output_2 = random.choice(verb_j);

            elif user_letters[2] == "k":
                output_2 = random.choice(verb_k);

            elif user_letters[2] == "l":
                output_2 = random.choice(verb_l);

            elif user_letters[2] == "m":
                output_2 = random.choice(verb_m);       

            elif user_letters[2] == "n":
                output_2 = random.choice(verb_n);

            elif user_letters[2] == "o":
                output_2 = random.choice(verb_o);    

            elif user_letters[2] == "p":
                output_2 = random.choice(verb_p);

            elif user_letters[2] == "q":
                output_2 = random.choice(verb_q);

            elif user_letters[2] == "r":
                output_2 = random.choice(verb_r);

            elif user_letters[2] == "s":
                output_2 = random.choice(verb_s);

            elif user_letters[2] == "t":
                output_2 = random.choice(verb_t);

            elif user_letters[2] == "u":
                output_2 = random.choice(verb_u);

            elif user_letters[2] == "v":
                output_2 = random.choice(verb_v);

            elif user_letters[2] == "w":
                output_2 = random.choice(verb_w);

            elif user_letters[2] == "x":
                output_2 = random.choice(verb_x);

            elif user_letters[2] == "y":
                output_2 = random.choice(verb_y);

            elif user_letters[2] == "z":
                output_2 = random.choice(verb_z);
        #adjective_3
            if user_letters[3] == "a":
                output_3 = random.choice(adjective_a);
                    
            elif user_letters[3] == "b":
                output_3 = random.choice(adjective_b);
                    
            elif user_letters[3] == "c":
                output_3 = random.choice(adjective_c);

            elif user_letters[3] == "d":
                output_3 = random.choice(adjective_d);

            elif user_letters[3] == "e":
                output_3 = random.choice(adjective_e);

            elif user_letters[3] == "f":
                output_3 = random.choice(adjective_f);

            elif user_letters[3] == "g":
                output_3 = random.choice(adjective_g);

            elif user_letters[3] == "h":
                output_3 = random.choice(adjective_h);

            elif user_letters[3] == "i":
                output_3 = random.choice(adjective_i);

            elif user_letters[3] == "j":
                output_3 = random.choice(adjective_j);

            elif user_letters[3] == "k":
                output_3 = random.choice(adjective_k);

            elif user_letters[3] == "l":
                output_3 = random.choice(adjective_l);

            elif user_letters[3] == "m":
                output_3 = random.choice(adjective_m);       

            elif user_letters[3] == "n":
                output_3 = random.choice(adjective_n);

            elif user_letters[3] == "o":
                output_3 = random.choice(adjective_o);    

            elif user_letters[3] == "p":
                output_3 = random.choice(adjective_p);

            elif user_letters[3] == "q":
                output_3 = random.choice(adjective_q);

            elif user_letters[3] == "r":
                output_3 = random.choice(adjective_r);

            elif user_letters[3] == "s":
                output_3 = random.choice(adjective_s);

            elif user_letters[3] == "t":
                output_3 = random.choice(adjective_t);

            elif user_letters[3] == "u":
                output_3 = random.choice(adjective_u);

            elif user_letters[3] == "v":
                output_3 = random.choice(adjective_v);

            elif user_letters[3] == "w":
                output_3 = random.choice(adjective_w);

            elif user_letters[3] == "x":
                output_3 = random.choice(adjective_x);

            elif user_letters[3] == "y":
                output_3 = random.choice(adjective_y);

            elif user_letters[3] == "z":
                output_3 = random.choice(adjective_z);
        #noun_4
            if "a" in user_letters:
                output_4 = random.choice(noun_a);
                
            elif "b" in user_letters:
                output_4 = random.choice(noun_b);

            elif "c" in user_letters:
                output_4 = random.choice(noun_c);

            elif "d" in user_letters:
                output_4 = random.choice(noun_d);

            elif "e" in user_letters:
                output_4 = random.choice(noun_e);

            elif "f" in user_letters:
                output_4 = random.choice(noun_f);

            elif "g" in user_letters:
                output_4 = random.choice(noun_g);

            elif "h" in user_letters:
                output_4 = random.choice(noun_h);

            elif "i" in user_letters:
                output_4 = random.choice(noun_i);

            elif "j" in user_letters:
                output_4 = random.choice(noun_j);

            elif "k" in user_letters:
                output_4 = random.choice(noun_k);

            elif "l" in user_letters:
                output_4 = random.choice(noun_l);

            elif "m" in user_letters:
                output_4 = random.choice(noun_m);         

            elif "n" in user_letters:
                output_4 = random.choice(noun_n);

            elif "o" in user_letters:
                output_4 = random.choice(noun_o);

            elif "p" in user_letters:
                output_4 = random.choice(noun_p);   

            elif "q" in user_letters:
                output_4 = random.choice(noun_q);   

            elif "r" in user_letters:
                output_4 = random.choice(noun_r);   

            elif "s" in user_letters:
                output_4 = random.choice(noun_s);   

            elif "t" in user_letters:
                output_4 = random.choice(noun_t);   

            elif "u" in user_letters:
                output_4 = random.choice(noun_u);   

            elif "v" in user_letters:
                output_4 = random.choice(noun_v);   

            elif "w" in user_letters:
                output_4 = random.choice(noun_w);   

            elif "x" in user_letters:
                output_4 = random.choice(noun_x);   

            elif "y" in user_letters:
                output_4 = random.choice(noun_y);   

            elif "z" in user_letters:
                output_4 = random.choice(noun_z);
        #print
            print (output_0, output_1, output_2, output_3, output_4);
            break

    #6 letters
        elif len(user_letters) == 6:
        #adjective_0
            if user_letters[0] == "a":
                output_0 = random.choice(adjective_a)
                adjective_a.remove(output_0);
                    
            elif user_letters[0] == "b":
                output_0 = random.choice(adjective_b)
                adjective_b.remove(output_0);
                    
            elif user_letters[0] == "c":
                output_0 = random.choice(adjective_c)
                adjective_c.remove(output_0);

            elif user_letters[0] == "d":
                output_0 = random.choice(adjective_d)
                adjective_d.remove(output_0);

            elif user_letters[0] == "e":
                output_0 = random.choice(adjective_e)
                adjective_e.remove(output_0);

            elif user_letters[0] == "f":
                output_0 = random.choice(adjective_f)
                adjective_f.remove(output_0);

            elif user_letters[0] == "g":
                output_0 = random.choice(adjective_g)
                adjective_g.remove(output_0);

            elif user_letters[0] == "h":
                output_0 = random.choice(adjective_h)
                adjective_h.remove(output_0);

            elif user_letters[0] == "i":
                output_0 = random.choice(adjective_i)
                adjective_i.remove(output_0);

            elif user_letters[0] == "j":
                output_0 = random.choice(adjective_j)
                adjective_j.remove(output_0);

            elif user_letters[0] == "k":
                output_0 = random.choice(adjective_k)
                adjective_k.remove(output_0);

            elif user_letters[0] == "l":
                output_0 = random.choice(adjective_l)
                adjective_l.remove(output_0);

            elif user_letters[0] == "m":
                output_0 = random.choice(adjective_m)
                adjective_m.remove(output_0);       

            elif user_letters[0] == "n":
                output_0 = random.choice(adjective_n)
                adjective_n.remove(output_0);

            elif user_letters[0] == "o":
                output_0 = random.choice(adjective_o)
                adjective_o.remove(output_0);    

            elif user_letters[0] == "p":
                output_0 = random.choice(adjective_p)
                adjective_p.remove(output_0);

            elif user_letters[0] == "q":
                output_0 = random.choice(adjective_q)
                adjective_q.remove(output_0);

            elif user_letters[0] == "r":
                output_0 = random.choice(adjective_r)
                adjective_r.remove(output_0);

            elif user_letters[0] == "s":
                output_0 = random.choice(adjective_s)
                adjective_s.remove(output_0);

            elif user_letters[0] == "t":
                output_0 = random.choice(adjective_t)
                adjective_t.remove(output_0);

            elif user_letters[0] == "u":
                output_0 = random.choice(adjective_u)
                adjective_u.remove(output_0);

            elif user_letters[0] == "v":
                output_0 = random.choice(adjective_v)
                adjective_v.remove(output_0);

            elif user_letters[0] == "w":
                output_0 = random.choice(adjective_w)
                adjective_w.remove(output_0);

            elif user_letters[0] == "x":
                output_0 = random.choice(adjective_x)
                adjective_x.remove(output_0);

            elif user_letters[0] == "y":
                output_0 = random.choice(adjective_y)
                adjective_y.remove(output_0);

            elif user_letters[0] == "z":
                output_0 = random.choice(adjective_z)
                adjective_z.remove(output_0);         
        #noun_1
            if "a" in user_letters:
                output_1 = random.choice(noun_a)
                noun_a.remove(output_1);
                
            elif "b" in user_letters:
                output_1 = random.choice(noun_b)
                noun_b.remove(output_1);

            elif "c" in user_letters:
                output_1 = random.choice(noun_c)
                noun_c.remove(output_1);

            elif "d" in user_letters:
                output_1 = random.choice(noun_d)
                noun_d.remove(output_1);

            elif "e" in user_letters:
                output_1 = random.choice(noun_e)
                noun_e.remove(output_1);

            elif "f" in user_letters:
                output_1 = random.choice(noun_f)
                noun_f.remove(output_1);

            elif "g" in user_letters:
                output_1 = random.choice(noun_g)
                noun_g.remove(output_1);

            elif "h" in user_letters:
                output_1 = random.choice(noun_h)
                noun_h.remove(output_1);

            elif "i" in user_letters:
                output_1 = random.choice(noun_i)
                noun_i.remove(output_1);

            elif "j" in user_letters:
                output_1 = random.choice(noun_j)
                noun_j.remove(output_1);

            elif "k" in user_letters:
                output_1 = random.choice(noun_k)
                noun_k.remove(output_1);

            elif "l" in user_letters:
                output_1 = random.choice(noun_l)
                noun_l.remove(output_1);

            elif "m" in user_letters:
                output_1 = random.choice(noun_m)
                noun_m.remove(output_1);         

            elif "n" in user_letters:
                output_1 = random.choice(noun_n)
                noun_n.remove(output_1);

            elif "o" in user_letters:
                output_1 = random.choice(noun_o)
                noun_o.remove(output_1);

            elif "p" in user_letters:
                output_1 = random.choice(noun_p)
                noun_p.remove(output_1);   

            elif "q" in user_letters:
                output_1 = random.choice(noun_q)
                noun_q.remove(output_1);   

            elif "r" in user_letters:
                output_1 = random.choice(noun_r)
                noun_r.remove(output_1);   

            elif "s" in user_letters:
                output_1 = random.choice(noun_s)
                noun_s.remove(output_1);   

            elif "t" in user_letters:
                output_1 = random.choice(noun_t)
                noun_t.remove(output_1);   

            elif "u" in user_letters:
                output_1 = random.choice(noun_u)
                noun_u.remove(output_1);   

            elif "v" in user_letters:
                output_1 = random.choice(noun_v)
                noun_v.remove(output_1);   

            elif "w" in user_letters:
                output_1 = random.choice(noun_w)
                noun_w.remove(output_1);   

            elif "x" in user_letters:
                output_1 = random.choice(noun_x)
                noun_x.remove(output_1);   

            elif "y" in user_letters:
                output_1 = random.choice(noun_y)
                noun_y.remove(output_1);   

            elif "z" in user_letters:
                output_1 = random.choice(noun_z)
                noun_z.remove(output_1);        
        #verb_2
            if user_letters[2] == "a":
                output_2 = random.choice(verb_a);
                    
            elif user_letters[2] == "b":
                output_2 = random.choice(verb_b);
                    
            elif user_letters[2] == "c":
                output_2 = random.choice(verb_c);

            elif user_letters[2] == "d":
                output_2 = random.choice(verb_d);

            elif user_letters[2] == "e":
                output_2 = random.choice(verb_e);

            elif user_letters[2] == "f":
                output_2 = random.choice(verb_f);

            elif user_letters[2] == "g":
                output_2 = random.choice(verb_g);

            elif user_letters[2] == "h":
                output_2 = random.choice(verb_h);

            elif user_letters[2] == "i":
                output_2 = random.choice(verb_i);

            elif user_letters[2] == "j":
                output_2 = random.choice(verb_j);

            elif user_letters[2] == "k":
                output_2 = random.choice(verb_k);

            elif user_letters[2] == "l":
                output_2 = random.choice(verb_l);

            elif user_letters[2] == "m":
                output_2 = random.choice(verb_m);       

            elif user_letters[2] == "n":
                output_2 = random.choice(verb_n);

            elif user_letters[2] == "o":
                output_2 = random.choice(verb_o);    

            elif user_letters[2] == "p":
                output_2 = random.choice(verb_p);

            elif user_letters[2] == "q":
                output_2 = random.choice(verb_q);

            elif user_letters[2] == "r":
                output_2 = random.choice(verb_r);

            elif user_letters[2] == "s":
                output_2 = random.choice(verb_s);

            elif user_letters[2] == "t":
                output_2 = random.choice(verb_t);

            elif user_letters[2] == "u":
                output_2 = random.choice(verb_u);

            elif user_letters[2] == "v":
                output_2 = random.choice(verb_v);

            elif user_letters[2] == "w":
                output_2 = random.choice(verb_w);

            elif user_letters[2] == "x":
                output_2 = random.choice(verb_x);

            elif user_letters[2] == "y":
                output_2 = random.choice(verb_y);

            elif user_letters[2] == "z":
                output_2 = random.choice(verb_z);
        #adjective_3
            if user_letters[3] == "a":
                output_3 = random.choice(adjective_a)
                adjective_a.remove(output_3);
                    
            elif user_letters[3] == "b":
                output_3 = random.choice(adjective_b)
                adjective_b.remove(output_3);
                    
            elif user_letters[3] == "c":
                output_3 = random.choice(adjective_c)
                adjective_c.remove(output_3);

            elif user_letters[3] == "d":
                output_3 = random.choice(adjective_d)
                adjective_d.remove(output_3);

            elif user_letters[3] == "e":
                output_3 = random.choice(adjective_e)
                adjective_e.remove(output_3);

            elif user_letters[3] == "f":
                output_3 = random.choice(adjective_f)
                adjective_f.remove(output_3);

            elif user_letters[3] == "g":
                output_3 = random.choice(adjective_g)
                adjective_g.remove(output_3);

            elif user_letters[3] == "h":
                output_3 = random.choice(adjective_h)
                adjective_h.remove(output_3);

            elif user_letters[3] == "i":
                output_3 = random.choice(adjective_i)
                adjective_i.remove(output_3);

            elif user_letters[3] == "j":
                output_3 = random.choice(adjective_j)
                adjective_j.remove(output_3);

            elif user_letters[3] == "k":
                output_3 = random.choice(adjective_k)
                adjective_k.remove(output_3);

            elif user_letters[3] == "l":
                output_3 = random.choice(adjective_l)
                adjective_l.remove(output_3);

            elif user_letters[3] == "m":
                output_3 = random.choice(adjective_m)
                adjective_m.remove(output_3);       

            elif user_letters[3] == "n":
                output_3 = random.choice(adjective_n)
                adjective_n.remove(output_3);

            elif user_letters[3] == "o":
                output_3 = random.choice(adjective_o)
                adjective_o.remove(output_3);    

            elif user_letters[3] == "p":
                output_3 = random.choice(adjective_p)
                adjective_p.remove(output_3);

            elif user_letters[3] == "q":
                output_3 = random.choice(adjective_q)
                adjective_q.remove(output_3);

            elif user_letters[3] == "r":
                output_3 = random.choice(adjective_r)
                adjective_r.remove(output_3);

            elif user_letters[3] == "s":
                output_3 = random.choice(adjective_s)
                adjective_s.remove(output_3);

            elif user_letters[3] == "t":
                output_3 = random.choice(adjective_t)
                adjective_t.remove(output_3);

            elif user_letters[3] == "u":
                output_3 = random.choice(adjective_u)
                adjective_u.remove(output_3);

            elif user_letters[3] == "v":
                output_3 = random.choice(adjective_v)
                adjective_v.remove(output_3);

            elif user_letters[3] == "w":
                output_3 = random.choice(adjective_w)
                adjective_w.remove(output_3);

            elif user_letters[3] == "x":
                output_3 = random.choice(adjective_x)
                adjective_x.remove(output_3);

            elif user_letters[3] == "y":
                output_3 = random.choice(adjective_y)
                adjective_y.remove(output_3);

            elif user_letters[3] == "z":
                output_3 = random.choice(adjective_z)
                adjective_z.remove(output_3);
        #adjective_4
            if user_letters[4] == "a":
                output_4 = random.choice(adjective_a);
                    
            elif user_letters[4] == "b":
                output_4 = random.choice(adjective_b);
                    
            elif user_letters[4] == "c":
                output_4 = random.choice(adjective_c);

            elif user_letters[4] == "d":
                output_4 = random.choice(adjective_d);

            elif user_letters[4] == "e":
                output_4 = random.choice(adjective_e);

            elif user_letters[4] == "f":
                output_4 = random.choice(adjective_f);

            elif user_letters[4] == "g":
                output_4 = random.choice(adjective_g);

            elif user_letters[4] == "h":
                output_4 = random.choice(adjective_h);

            elif user_letters[4] == "i":
                output_4 = random.choice(adjective_i);

            elif user_letters[4] == "j":
                output_4 = random.choice(adjective_j);

            elif user_letters[4] == "k":
                output_4 = random.choice(adjective_k);

            elif user_letters[4] == "l":
                output_4 = random.choice(adjective_l);

            elif user_letters[4] == "m":
                output_4 = random.choice(adjective_m);       

            elif user_letters[4] == "n":
                output_4 = random.choice(adjective_n);

            elif user_letters[4] == "o":
                output_4 = random.choice(adjective_o);    

            elif user_letters[4] == "p":
                output_4 = random.choice(adjective_p);

            elif user_letters[4] == "q":
                output_4 = random.choice(adjective_q);

            elif user_letters[4] == "r":
                output_4 = random.choice(adjective_r);

            elif user_letters[4] == "s":
                output_4 = random.choice(adjective_s);

            elif user_letters[4] == "t":
                output_4 = random.choice(adjective_t);

            elif user_letters[4] == "u":
                output_4 = random.choice(adjective_u);

            elif user_letters[4] == "v":
                output_4 = random.choice(adjective_v);

            elif user_letters[4] == "w":
                output_4 = random.choice(adjective_w);

            elif user_letters[4] == "x":
                output_4 = random.choice(adjective_x);

            elif user_letters[4] == "y":
                output_4 = random.choice(adjective_y);

            elif user_letters[4] == "z":
                output_4 = random.choice(adjective_z);
        #noun_5
            if "a" in user_letters:
                output_5 = random.choice(noun_a);
                
            elif "b" in user_letters:
                output_5 = random.choice(noun_b);

            elif "c" in user_letters:
                output_5 = random.choice(noun_c);

            elif "d" in user_letters:
                output_5 = random.choice(noun_d);

            elif "e" in user_letters:
                output_5 = random.choice(noun_e);

            elif "f" in user_letters:
                output_5 = random.choice(noun_f);

            elif "g" in user_letters:
                output_5 = random.choice(noun_g);

            elif "h" in user_letters:
                output_5 = random.choice(noun_h);

            elif "i" in user_letters:
                output_5 = random.choice(noun_i);

            elif "j" in user_letters:
                output_5 = random.choice(noun_j);

            elif "k" in user_letters:
                output_5 = random.choice(noun_k);

            elif "l" in user_letters:
                output_5 = random.choice(noun_l);

            elif "m" in user_letters:
                output_5 = random.choice(noun_m);         

            elif "n" in user_letters:
                output_5 = random.choice(noun_n);

            elif "o" in user_letters:
                output_5 = random.choice(noun_o);

            elif "p" in user_letters:
                output_5 = random.choice(noun_p);   

            elif "q" in user_letters:
                output_5 = random.choice(noun_q);   

            elif "r" in user_letters:
                output_5 = random.choice(noun_r);   

            elif "s" in user_letters:
                output_5 = random.choice(noun_s);   

            elif "t" in user_letters:
                output_5 = random.choice(noun_t);   

            elif "u" in user_letters:
                output_5 = random.choice(noun_u);   

            elif "v" in user_letters:
                output_5 = random.choice(noun_v);   

            elif "w" in user_letters:
                output_5 = random.choice(noun_w);   

            elif "x" in user_letters:
                output_5 = random.choice(noun_x);   

            elif "y" in user_letters:
                output_5 = random.choice(noun_y);   

            elif "z" in user_letters:
                output_5 = random.choice(noun_z);
        #print
            print (output_0, output_1, output_2, output_3, output_4, output_5);
            break
            
    #7 letters
  
        elif len(user_letters) == 7:
            if user_letters[0] == "a":
                output_0 = random.choice(adjective_a)
                adjective_a.remove(output_0);
                    
            elif user_letters[0] == "b":
                output_0 = random.choice(adjective_b)
                adjective_b.remove(output_0);
                    
            elif user_letters[0] == "c":
                output_0 = random.choice(adjective_c)
                adjective_c.remove(output_0);

            elif user_letters[0] == "d":
                output_0 = random.choice(adjective_d)
                adjective_d.remove(output_0);

            elif user_letters[0] == "e":
                output_0 = random.choice(adjective_e)
                adjective_e.remove(output_0);

            elif user_letters[0] == "f":
                output_0 = random.choice(adjective_f)
                adjective_f.remove(output_0);

            elif user_letters[0] == "g":
                output_0 = random.choice(adjective_g)
                adjective_g.remove(output_0);

            elif user_letters[0] == "h":
                output_0 = random.choice(adjective_h)
                adjective_h.remove(output_0);

            elif user_letters[0] == "i":
                output_0 = random.choice(adjective_i)
                adjective_i.remove(output_0);

            elif user_letters[0] == "j":
                output_0 = random.choice(adjective_j)
                adjective_j.remove(output_0);

            elif user_letters[0] == "k":
                output_0 = random.choice(adjective_k)
                adjective_k.remove(output_0);

            elif user_letters[0] == "l":
                output_0 = random.choice(adjective_l)
                adjective_l.remove(output_0);

            elif user_letters[0] == "m":
                output_0 = random.choice(adjective_m)
                adjective_m.remove(output_0);       

            elif user_letters[0] == "n":
                output_0 = random.choice(adjective_n)
                adjective_n.remove(output_0);

            elif user_letters[0] == "o":
                output_0 = random.choice(adjective_o)
                adjective_o.remove(output_0);    

            elif user_letters[0] == "p":
                output_0 = random.choice(adjective_p)
                adjective_p.remove(output_0);

            elif user_letters[0] == "q":
                output_0 = random.choice(adjective_q)
                adjective_q.remove(output_0);

            elif user_letters[0] == "r":
                output_0 = random.choice(adjective_r)
                adjective_r.remove(output_0);

            elif user_letters[0] == "s":
                output_0 = random.choice(adjective_s)
                adjective_s.remove(output_0);

            elif user_letters[0] == "t":
                output_0 = random.choice(adjective_t)
                adjective_t.remove(output_0);

            elif user_letters[0] == "u":
                output_0 = random.choice(adjective_u)
                adjective_u.remove(output_0);

            elif user_letters[0] == "v":
                output_0 = random.choice(adjective_v)
                adjective_v.remove(output_0);

            elif user_letters[0] == "w":
                output_0 = random.choice(adjective_w)
                adjective_w.remove(output_0);

            elif user_letters[0] == "x":
                output_0 = random.choice(adjective_x)
                adjective_x.remove(output_0);

            elif user_letters[0] == "y":
                output_0 = random.choice(adjective_y)
                adjective_y.remove(output_0);

            elif user_letters[0] == "z":
                output_0 = random.choice(adjective_z)
                adjective_z.remove(output_0);         
        #adjective_0
            if user_letters[0] == "a":
                output_0 = random.choice(adjective_a)
                adjective_a.remove(output_0);
                    
            elif user_letters[0] == "b":
                output_0 = random.choice(adjective_b)
                adjective_b.remove(output_0);
                    
            elif user_letters[0] == "c":
                output_0 = random.choice(adjective_c)
                adjective_c.remove(output_0);

            elif user_letters[0] == "d":
                output_0 = random.choice(adjective_d)
                adjective_d.remove(output_0);

            elif user_letters[0] == "e":
                output_0 = random.choice(adjective_e)
                adjective_e.remove(output_0);

            elif user_letters[0] == "f":
                output_0 = random.choice(adjective_f)
                adjective_f.remove(output_0);

            elif user_letters[0] == "g":
                output_0 = random.choice(adjective_g)
                adjective_g.remove(output_0);

            elif user_letters[0] == "h":
                output_0 = random.choice(adjective_h)
                adjective_h.remove(output_0);

            elif user_letters[0] == "i":
                output_0 = random.choice(adjective_i)
                adjective_i.remove(output_0);

            elif user_letters[0] == "j":
                output_0 = random.choice(adjective_j)
                adjective_j.remove(output_0);

            elif user_letters[0] == "k":
                output_0 = random.choice(adjective_k)
                adjective_k.remove(output_0);

            elif user_letters[0] == "l":
                output_0 = random.choice(adjective_l)
                adjective_l.remove(output_0);

            elif user_letters[0] == "m":
                output_0 = random.choice(adjective_m)
                adjective_m.remove(output_0);       

            elif user_letters[0] == "n":
                output_0 = random.choice(adjective_n)
                adjective_n.remove(output_0);

            elif user_letters[0] == "o":
                output_0 = random.choice(adjective_o)
                adjective_o.remove(output_0);    

            elif user_letters[0] == "p":
                output_0 = random.choice(adjective_p)
                adjective_p.remove(output_0);

            elif user_letters[0] == "q":
                output_0 = random.choice(adjective_q)
                adjective_q.remove(output_0);

            elif user_letters[0] == "r":
                output_0 = random.choice(adjective_r)
                adjective_r.remove(output_0);

            elif user_letters[0] == "s":
                output_0 = random.choice(adjective_s)
                adjective_s.remove(output_0);

            elif user_letters[0] == "t":
                output_0 = random.choice(adjective_t)
                adjective_t.remove(output_0);

            elif user_letters[0] == "u":
                output_0 = random.choice(adjective_u)
                adjective_u.remove(output_0);

            elif user_letters[0] == "v":
                output_0 = random.choice(adjective_v)
                adjective_v.remove(output_0);

            elif user_letters[0] == "w":
                output_0 = random.choice(adjective_w)
                adjective_w.remove(output_0);

            elif user_letters[0] == "x":
                output_0 = random.choice(adjective_x)
                adjective_x.remove(output_0);

            elif user_letters[0] == "y":
                output_0 = random.choice(adjective_y)
                adjective_y.remove(output_0);

            elif user_letters[0] == "z":
                output_0 = random.choice(adjective_z)
                adjective_z.remove(output_0);         
        #adjective_1
            if user_letters[1] == "a":
                output_1 = random.choice(adjective_a)
                adjective_a.remove(output_1);
                    
            elif user_letters[1] == "b":
                output_1 = random.choice(adjective_b)
                adjective_b.remove(output_1);
                    
            elif user_letters[1] == "c":
                output_1 = random.choice(adjective_c)
                adjective_c.remove(output_1);

            elif user_letters[1] == "d":
                output_1 = random.choice(adjective_d)
                adjective_d.remove(output_1);

            elif user_letters[1] == "e":
                output_1 = random.choice(adjective_e)
                adjective_e.remove(output_1);

            elif user_letters[1] == "f":
                output_1 = random.choice(adjective_f)
                adjective_f.remove(output_1);

            elif user_letters[1] == "g":
                output_1 = random.choice(adjective_g)
                adjective_g.remove(output_1);

            elif user_letters[1] == "h":
                output_1 = random.choice(adjective_h)
                adjective_h.remove(output_1);

            elif user_letters[1] == "i":
                output_1 = random.choice(adjective_i)
                adjective_i.remove(output_1);

            elif user_letters[1] == "j":
                output_1 = random.choice(adjective_j)
                adjective_j.remove(output_1);

            elif user_letters[1] == "k":
                output_1 = random.choice(adjective_k)
                adjective_k.remove(output_1);

            elif user_letters[1] == "l":
                output_1 = random.choice(adjective_l)
                adjective_l.remove(output_1);

            elif user_letters[1] == "m":
                output_1 = random.choice(adjective_m)
                adjective_m.remove(output_1);       

            elif user_letters[1] == "n":
                output_1 = random.choice(adjective_n)
                adjective_n.remove(output_1);

            elif user_letters[1] == "o":
                output_1 = random.choice(adjective_o)
                adjective_o.remove(output_1);    

            elif user_letters[1] == "p":
                output_1 = random.choice(adjective_p)
                adjective_p.remove(output_1);

            elif user_letters[1] == "q":
                output_1 = random.choice(adjective_q)
                adjective_q.remove(output_1);

            elif user_letters[1] == "r":
                output_1 = random.choice(adjective_r)
                adjective_r.remove(output_1);

            elif user_letters[1] == "s":
                output_1 = random.choice(adjective_s)
                adjective_s.remove(output_1);

            elif user_letters[1] == "t":
                output_1 = random.choice(adjective_t)
                adjective_t.remove(output_1);

            elif user_letters[1] == "u":
                output_1 = random.choice(adjective_u)
                adjective_u.remove(output_1);

            elif user_letters[1] == "v":
                output_1 = random.choice(adjective_v)
                adjective_v.remove(output_1);

            elif user_letters[1] == "w":
                output_1 = random.choice(adjective_w)
                adjective_w.remove(output_1);

            elif user_letters[1] == "x":
                output_1 = random.choice(adjective_x)
                adjective_x.remove(output_1);

            elif user_letters[1] == "y":
                output_1 = random.choice(adjective_y)
                adjective_y.remove(output_1);

            elif user_letters[1] == "z":
                output_1 = random.choice(adjective_z)
                adjective_z.remove(output_1);
        #noun_2
            if "a" in user_letters:
                output_2 = random.choice(noun_a)
                noun_a.remove(output_2);
                
            elif "b" in user_letters:
                output_2 = random.choice(noun_b)
                noun_b.remove(output_2);

            elif "c" in user_letters:
                output_2 = random.choice(noun_c)
                noun_c.remove(output_2);

            elif "d" in user_letters:
                output_2 = random.choice(noun_d)
                noun_d.remove(output_2);

            elif "e" in user_letters:
                output_2 = random.choice(noun_e)
                noun_e.remove(output_2);

            elif "f" in user_letters:
                output_2 = random.choice(noun_f)
                noun_f.remove(output_2);

            elif "g" in user_letters:
                output_2 = random.choice(noun_g)
                noun_g.remove(output_2);

            elif "h" in user_letters:
                output_2 = random.choice(noun_h)
                noun_h.remove(output_2);

            elif "i" in user_letters:
                output_2 = random.choice(noun_i)
                noun_i.remove(output_2);

            elif "j" in user_letters:
                output_2 = random.choice(noun_j)
                noun_j.remove(output_2);

            elif "k" in user_letters:
                output_2 = random.choice(noun_k)
                noun_k.remove(output_2);

            elif "l" in user_letters:
                output_2 = random.choice(noun_l)
                noun_l.remove(output_2);

            elif "m" in user_letters:
                output_2 = random.choice(noun_m)
                noun_m.remove(output_2);         

            elif "n" in user_letters:
                output_2 = random.choice(noun_n)
                noun_n.remove(output_2);

            elif "o" in user_letters:
                output_2 = random.choice(noun_o)
                noun_o.remove(output_2);

            elif "p" in user_letters:
                output_2 = random.choice(noun_p)
                noun_p.remove(output_2);   

            elif "q" in user_letters:
                output_2 = random.choice(noun_q)
                noun_q.remove(output_2);   

            elif "r" in user_letters:
                output_2 = random.choice(noun_r)
                noun_r.remove(output_2);   

            elif "s" in user_letters:
                output_2 = random.choice(noun_s)
                noun_s.remove(output_2);   

            elif "t" in user_letters:
                output_2 = random.choice(noun_t)
                noun_t.remove(output_2);   

            elif "u" in user_letters:
                output_2 = random.choice(noun_u)
                noun_u.remove(output_2);   

            elif "v" in user_letters:
                output_2 = random.choice(noun_v)
                noun_v.remove(output_2);   

            elif "w" in user_letters:
                output_2 = random.choice(noun_w)
                noun_w.remove(output_2);   

            elif "x" in user_letters:
                output_2 = random.choice(noun_x)
                noun_x.remove(output_2);   

            elif "y" in user_letters:
                output_2 = random.choice(noun_y)
                noun_y.remove(output_2);   

            elif "z" in user_letters:
                output_2 = random.choice(noun_z)
                noun_z.remove(output_2);        
        #verb_3
            if user_letters[3] == "a":
                output_3 = random.choice(verb_a);
                    
            elif user_letters[3] == "b":
                output_3 = random.choice(verb_b);
                    
            elif user_letters[3] == "c":
                output_3 = random.choice(verb_c);

            elif user_letters[3] == "d":
                output_3 = random.choice(verb_d);

            elif user_letters[3] == "e":
                output_3 = random.choice(verb_e);

            elif user_letters[3] == "f":
                output_3 = random.choice(verb_f);

            elif user_letters[3] == "g":
                output_3 = random.choice(verb_g);

            elif user_letters[3] == "h":
                output_3 = random.choice(verb_h);

            elif user_letters[3] == "i":
                output_3 = random.choice(verb_i);

            elif user_letters[3] == "i":
                output_3 = random.choice(verb_i);

            elif user_letters[3] == "j":
                output_3 = random.choice(verb_j);

            elif user_letters[3] == "k":
                output_3 = random.choice(verb_k);

            elif user_letters[3] == "l":
                output_3 = random.choice(verb_l);

            elif user_letters[3] == "m":
                output_3 = random.choice(verb_m);       

            elif user_letters[3] == "n":
                output_3 = random.choice(verb_n);

            elif user_letters[3] == "o":
                output_3 = random.choice(verb_o);    

            elif user_letters[3] == "p":
                output_3 = random.choice(verb_p);

            elif user_letters[3] == "q":
                output_3 = random.choice(verb_q);

            elif user_letters[3] == "r":
                output_3 = random.choice(verb_r);

            elif user_letters[3] == "s":
                output_3 = random.choice(verb_s);

            elif user_letters[3] == "t":
                output_3 = random.choice(verb_t);

            elif user_letters[3] == "u":
                output_3 = random.choice(verb_u);

            elif user_letters[3] == "v":
                output_3 = random.choice(verb_v);

            elif user_letters[3] == "w":
                output_3 = random.choice(verb_w);

            elif user_letters[3] == "x":
                output_3 = random.choice(verb_x);

            elif user_letters[3] == "y":
                output_3 = random.choice(verb_y);

            elif user_letters[3] == "z":
                output_3 = random.choice(verb_z);
        #adjective_4
            if user_letters[4] == "a":
                output_4 = random.choice(adjective_a)
                adjective_a.remove(output_4);
                    
            elif user_letters[4] == "b":
                output_4 = random.choice(adjective_b)
                adjective_b.remove(output_4);
                    
            elif user_letters[4] == "c":
                output_4 = random.choice(adjective_c)
                adjective_c.remove(output_4);

            elif user_letters[4] == "d":
                output_4 = random.choice(adjective_d)
                adjective_d.remove(output_4);

            elif user_letters[4] == "e":
                output_4 = random.choice(adjective_e)
                adjective_e.remove(output_4);

            elif user_letters[4] == "f":
                output_4 = random.choice(adjective_f)
                adjective_f.remove(output_4);

            elif user_letters[4] == "g":
                output_4 = random.choice(adjective_g)
                adjective_g.remove(output_4);

            elif user_letters[4] == "h":
                output_4 = random.choice(adjective_h)
                adjective_h.remove(output_4);

            elif user_letters[4] == "i":
                output_4 = random.choice(adjective_i)
                adjective_i.remove(output_4);

            elif user_letters[4] == "j":
                output_4 = random.choice(adjective_j)
                adjective_j.remove(output_4);

            elif user_letters[4] == "k":
                output_4 = random.choice(adjective_k)
                adjective_k.remove(output_4);

            elif user_letters[4] == "l":
                output_4 = random.choice(adjective_l)
                adjective_l.remove(output_4);

            elif user_letters[4] == "m":
                output_4 = random.choice(adjective_m)
                adjective_m.remove(output_4);       

            elif user_letters[4] == "n":
                output_4 = random.choice(adjective_n)
                adjective_n.remove(output_4);

            elif user_letters[4] == "o":
                output_4 = random.choice(adjective_o)
                adjective_o.remove(output_4);    

            elif user_letters[4] == "p":
                output_4 = random.choice(adjective_p)
                adjective_p.remove(output_4);

            elif user_letters[4] == "q":
                output_4 = random.choice(adjective_q)
                adjective_q.remove(output_4);

            elif user_letters[4] == "r":
                output_4 = random.choice(adjective_r)
                adjective_r.remove(output_4);

            elif user_letters[4] == "s":
                output_4 = random.choice(adjective_s)
                adjective_s.remove(output_4);

            elif user_letters[4] == "t":
                output_4 = random.choice(adjective_t)
                adjective_t.remove(output_4);

            elif user_letters[4] == "u":
                output_4 = random.choice(adjective_u)
                adjective_u.remove(output_4);

            elif user_letters[4] == "v":
                output_4 = random.choice(adjective_v)
                adjective_v.remove(output_4);

            elif user_letters[4] == "w":
                output_4 = random.choice(adjective_w)
                adjective_w.remove(output_4);

            elif user_letters[4] == "x":
                output_4 = random.choice(adjective_x)
                adjective_x.remove(output_4);

            elif user_letters[4] == "y":
                output_4 = random.choice(adjective_y)
                adjective_y.remove(output_4);

            elif user_letters[4] == "z":
                output_4 = random.choice(adjective_z)
                adjective_z.remove(output_4);
        #adjective_5
            if user_letters[5] == "a":
                output_5 = random.choice(adjective_a)
                adjective_a.remove(output_5);
                    
            elif user_letters[5] == "b":
                output_5 = random.choice(adjective_b)
                adjective_b.remove(output_5);
                    
            elif user_letters[5] == "c":
                output_5 = random.choice(adjective_c)
                adjective_c.remove(output_5);

            elif user_letters[5] == "d":
                output_5 = random.choice(adjective_d)
                adjective_d.remove(output_5);

            elif user_letters[5] == "e":
                output_5 = random.choice(adjective_e)
                adjective_e.remove(output_5);

            elif user_letters[5] == "f":
                output_5 = random.choice(adjective_f)
                adjective_f.remove(output_5);

            elif user_letters[5] == "g":
                output_5 = random.choice(adjective_g)
                adjective_g.remove(output_5);

            elif user_letters[5] == "h":
                output_5 = random.choice(adjective_h)
                adjective_h.remove(output_5);

            elif user_letters[5] == "i":
                output_5 = random.choice(adjective_i)
                adjective_i.remove(output_5);

            elif user_letters[5] == "j":
                output_5 = random.choice(adjective_j)
                adjective_j.remove(output_5);

            elif user_letters[5] == "k":
                output_5 = random.choice(adjective_k)
                adjective_k.remove(output_5);

            elif user_letters[5] == "l":
                output_5 = random.choice(adjective_l)
                adjective_l.remove(output_5);

            elif user_letters[5] == "m":
                output_5 = random.choice(adjective_m)
                adjective_m.remove(output_5);       

            elif user_letters[5] == "n":
                output_5 = random.choice(adjective_n)
                adjective_n.remove(output_5);

            elif user_letters[5] == "o":
                output_5 = random.choice(adjective_o)
                adjective_o.remove(output_5);    

            elif user_letters[5] == "p":
                output_5 = random.choice(adjective_p)
                adjective_p.remove(output_5);

            elif user_letters[5] == "q":
                output_5 = random.choice(adjective_q)
                adjective_q.remove(output_5);

            elif user_letters[5] == "r":
                output_5 = random.choice(adjective_r)
                adjective_r.remove(output_5);

            elif user_letters[5] == "s":
                output_5 = random.choice(adjective_s)
                adjective_s.remove(output_5);

            elif user_letters[5] == "t":
                output_5 = random.choice(adjective_t)
                adjective_t.remove(output_5);

            elif user_letters[5] == "u":
                output_5 = random.choice(adjective_u)
                adjective_u.remove(output_5);

            elif user_letters[5] == "v":
                output_5 = random.choice(adjective_v)
                adjective_v.remove(output_5);

            elif user_letters[5] == "w":
                output_5 = random.choice(adjective_w)
                adjective_w.remove(output_5);

            elif user_letters[5] == "x":
                output_5 = random.choice(adjective_x)
                adjective_x.remove(output_5);

            elif user_letters[5] == "y":
                output_5 = random.choice(adjective_y)
                adjective_y.remove(output_5);

            elif user_letters[5] == "z":
                output_5 = random.choice(adjective_z)
                adjective_z.remove(output_5);
        #noun_6
            if "a" in user_letters:
                output_6 = random.choice(noun_a)
                noun_a.remove(output_6);
                
            elif "b" in user_letters:
                output_6 = random.choice(noun_b)
                noun_b.remove(output_6);

            elif "c" in user_letters:
                output_6 = random.choice(noun_c)
                noun_c.remove(output_6);

            elif "d" in user_letters:
                output_6 = random.choice(noun_d)
                noun_d.remove(output_6);

            elif "e" in user_letters:
                output_6 = random.choice(noun_e)
                noun_e.remove(output_6);

            elif "f" in user_letters:
                output_6 = random.choice(noun_f)
                noun_f.remove(output_6);

            elif "g" in user_letters:
                output_6 = random.choice(noun_g)
                noun_g.remove(output_6);

            elif "h" in user_letters:
                output_6 = random.choice(noun_h)
                noun_h.remove(output_6);

            elif "i" in user_letters:
                output_6 = random.choice(noun_i)
                noun_i.remove(output_6);

            elif "j" in user_letters:
                output_6 = random.choice(noun_j)
                noun_j.remove(output_6);

            elif "k" in user_letters:
                output_6 = random.choice(noun_k)
                noun_k.remove(output_6);

            elif "l" in user_letters:
                output_6 = random.choice(noun_l)
                noun_l.remove(output_6);

            elif "m" in user_letters:
                output_6 = random.choice(noun_m)
                noun_m.remove(output_6);         

            elif "n" in user_letters:
                output_6 = random.choice(noun_n)
                noun_n.remove(output_6);

            elif "o" in user_letters:
                output_6 = random.choice(noun_o)
                noun_o.remove(output_6);

            elif "p" in user_letters:
                output_6 = random.choice(noun_p)
                noun_p.remove(output_6);   

            elif "q" in user_letters:
                output_6 = random.choice(noun_q)
                noun_q.remove(output_6);   

            elif "r" in user_letters:
                output_6 = random.choice(noun_r)
                noun_r.remove(output_6);   

            elif "s" in user_letters:
                output_6 = random.choice(noun_s)
                noun_s.remove(output_6);   

            elif "t" in user_letters:
                output_6 = random.choice(noun_t)
                noun_t.remove(output_6);   

            elif "u" in user_letters:
                output_6 = random.choice(noun_u)
                noun_u.remove(output_6);   

            elif "v" in user_letters:
                output_6 = random.choice(noun_v)
                noun_v.remove(output_6);   

            elif "w" in user_letters:
                output_6 = random.choice(noun_w)
                noun_w.remove(output_6);   

            elif "x" in user_letters:
                output_6 = random.choice(noun_x)
                noun_x.remove(output_6);   

            elif "y" in user_letters:
                output_6 = random.choice(noun_y)
                noun_y.remove(output_6);   

            elif "z" in user_letters:
                output_6 = random.choice(noun_z)
                noun_z.remove(output_6);        
        #print
            print (output_0, output_1, output_2, output_3, output_4, output_5, output_6);
            break

    else:
        print ("Don't know what you put in there but it wasn't letters.")

time.sleep(2) 
print ("Thank you for using this homemade mnemonic script!")        

    



