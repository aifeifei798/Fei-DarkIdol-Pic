import random

# --- V2.0 - Massively Expanded Keyword Categories ---

# Category 1: The Vibe & Personality
vibes = [
    "Alluring", "Captivating", "Charismatic", "Dynamic", "Electric", "Enigmatic", 
    "Magnetic", "Hypnotic", "A whole vibe", "Ethereal", "Unforgettable", "Mysterious", 
    "Radiant", "Confident", "Serene", "Cool", "Effortless", "Poised", "Sophisticated", "Glamorous"
]
menaces = [
    "Fierce", "Dangerous", "Edgy", "Rebellious", "Provocative", "Intense", "Unapologetic", 
    "Audacious", "Smoldering", "Defiant", "Untamable", "Wild", "Formidable", "Menacing", 
    "Seductive", "Commanding", "Dominant", "Lethal", "Icy", "Aloof"
]
firecrackers = [
    "Energetic", "Explosive", "Fiery", "Spirited", "Spunky", "Vibrant", "Volatile", 
    "Bold", "Feisty", "Vivacious", "Passionate", "Dynamic", "Impulsive", "Unpredictable", 
    "Charismatic", "Bubbly", "Lively", "Radiant", "Dazzling", "Playful"
]
dime_pieces = [
    "Stunning", "Gorgeous", "Flawless", "Exquisite", "Breathtaking", "Divine", "Head-turner", 
    "Showstopper", "A perfect 10", "Angelic", "God-tier visuals", "Otherworldly", "Ethereal beauty", 
    "Mesmerizing", "Picture-perfect", "Drop-dead gorgeous", "Irresistible", "Jaw-dropping", "Flawless", "Aphrodite"
]
bricks = [
    "Powerful", "Strong", "Athletic", "Sculpted", "Toned", "Solid", "Statuesque", "Well-built", 
    "Formidable physique", "Lean muscle", "Defined", "Fit", "Healthy", "Powerful stance", 
    "Confident posture", "Imposing", "Resilient", "Robust", "Amazonian", "Unbreakable"
]

# Clothing, Accessories & Swimwear

clothing = [
"a worn-in leather jacket with faded patches",
"a pair of ripped, light-wash skinny jeans",
"a chunky, oversized cable-knit sweater",
"a vintage band t-shirt, soft from years of wear",
"a tailored black blazer with satin lapels",
"a flowing, floral-print maxi dress",
"a pair of classic, scuffed-up combat boots",
"a crisp white button-down shirt, sleeves rolled up",
"a red silk evening gown with a thigh-high slit",
"a pair of high-waisted, wide-leg linen trousers",
"a distressed denim jacket with a sherpa collar",
"a simple gray crewneck sweatshirt",
"a plaid flannel shirt tied around the waist",
"a pair of sleek, black leather leggings",
"a vintage-style A-line swing dress",
"a pair of retro, high-top canvas sneakers",
"a cashmere turtleneck in a neutral color",
"a heavy wool peacoat against the cold",
"a delicate lace bralette peeking out from a shirt",
"a pair of tailored chino shorts",
"a fitted, black cocktail dress",
"a well-worn pair of leather loafers",
"a bohemian-style embroidered tunic",
"a dark wash denim skirt with a frayed hem",
"a hooded, waterproof rain slicker",
"a pair of platform heels in a bold color",
"a silk camisole with thin spaghetti straps",
"a pair of athletic joggers for a casual look",
"a structured trench coat, belted at the waist",
"a straw fedora hat for a sunny day",
"a pair of dark, raw denim selvedge jeans",
"a vibrant, patterned Hawaiian shirt",
"a pinstripe business suit",
"a pair of leather Chelsea boots",
"a velvet slip dress",
"an oversized, graphic-print hoodie",
"a pair of cat-eye sunglasses",
"a hand-knitted, colorful scarf",
"a sequined mini-dress for a night out",
"a pair of comfortable, worn-in Birkenstocks",
"a classic polo shirt",
"a faux fur coat in a dramatic color",
"a pair of corduroy pants",
"a simple, elegant gold chain necklace",
"a sporty bomber jacket with embroidered details",
"a pair of biker shorts worn under a blazer",
"a cropped, off-the-shoulder top",
"a pair of espadrille wedges",
"a utility jumpsuit in olive green",
"a delicate silver anklet",
"a tweed sport coat with elbow patches",
"a pair of overall jeans",
"a ribbed, form-fitting turtleneck dress",
"a pair of suede desert boots",
"a simple canvas tote bag with a witty slogan",
"a linen button-up shirt, slightly wrinkled",
"a pair of metallic silver ankle boots",
"a Goth-style corset top",
"a pair of baggy, 90s-style cargo pants",
"a hand-tooled leather belt with a silver buckle",
"a silk pajama set worn as daywear",
"a pair of track pants with side snaps",
"a classic Barbour waxed cotton jacket",
"a pair of delicate, strappy stiletto sandals",
"a tie-dye t-shirt, hand-made",
"a newsboy cap in herringbone wool",
"a pair of tailored, high-waisted paperbag shorts",
"a monogrammed, luxury leather handbag",
"a vintage bowling shirt with a name stitched on it",
"a sheer, see-through blouse over a camisole",
"a pair of white leather minimalist sneakers",
"a punk-rock style studded leather vest",
"a pair of oversized, academic-style eyeglasses",
"a long, pleated midi skirt",
"a pair of fisherman sandals",
"a heavy metal band hoodie, black and faded",
"a pair of brightly colored, patterned socks",
"a simple black one-piece swimsuit",
"a pair of polished leather Oxford dress shoes",
"a statement necklace with large, colorful beads",
"a military-style field jacket",
"a pair of velvet bell-bottom pants",
"a satin headscarf tied around the hair",
"a preppy argyle sweater vest",
"a pair of rugged, waterproof hiking boots",
"a tailored tuxedo with a bow tie",
"a pair of fishnet stockings",
"a fringed suede jacket",
"a pair of round, wire-rimmed glasses",
"a wrap dress in a jersey knit",
"a pair of shearling-lined slippers",
"a simple, understated silver ring",
"a denim vest covered in enamel pins",
"a pair of leather driving gloves",
"a cozy, full-body fleece onesie",
"a pair of vintage, high-waisted mom jeans",
"a bucket hat in a trendy pattern",
"a single, elegant pearl earring",
# --- New York Popular Style Additions ---
"an all-black monochrome outfit from head to toe",
"a designer handbag carried as a statement piece",
"a long, tailored wool overcoat in camel or grey",
"a pair of stylish, comfortable sneakers for walking the city",
"a vintage, oversized blazer with shoulder pads",
"a simple, high-quality t-shirt in white, black, or heather grey",
"a pair of sleek, ankle-length trousers",
"layered gold necklaces of varying lengths",
"a crossbody bag for hands-free convenience",
"a pair of statement sunglasses, even on a cloudy day",
"a muted-tone, minimalist sweatsuit set",
"a pair of wide-leg, floor-sweeping jeans",
"a leather trench coat",
"a puff-sleeve, romantic-style blouse",
"a pair of chunky-soled loafers",
"a baseball cap from a New York sports team",
"a cashmere beanie in winter",
"a pair of straight-leg, perfectly tailored black pants",
"a silk midi skirt paired with a casual sweater",
"a utility vest with multiple pockets",
# --- Bikini Additions ---
"a classic triangle string bikini in a solid bright color",
"a high-waisted retro bikini with a polka dot print",
"a strapless bandeau bikini top with matching bottoms",
"a sporty, racerback bikini designed for activity",
"a crochet, bohemian-style bikini",
"a one-shoulder bikini with an asymmetrical design",
"an animal print (leopard or snake) bikini",
"a bikini with ruffled straps and edges",
"a metallic, high-shine bikini for a glamorous look",
"a thong bikini bottom with minimal coverage",
"a cut-out one-piece that resembles a bikini",
"a halter top bikini that ties around the neck",
"a neon-colored bikini that stands out",
"a floral print bikini with a tropical vibe",
"a ribbed-fabric bikini for added texture",
"a tie-front bikini top with a small knot",
"a color-block bikini with contrasting panels",
"a longline bikini top that extends further down the torso",
"a micro-bikini with extremely small fabric panels",
"a velvet bikini for a luxurious, unconventional feel"
]

# Category 2: Subject & Appearance
subjects = [
    "K-pop Idol", "Korean model", "Pop star", "East Asian woman", "Solo artist", "K-pop dancer", 
    "Lead vocalist", "Korean actress", "Asian influencer", "Fashion icon", "It-girl", 
    "K-fashion model", "Seoulite", "Rising star", "Music sensation", "Urban muse", "Night crawler", "Style maven"
]
features = [
    "Sharp jawline", "Intense gaze", "Piercing eyes", "Confident expression", "Symmetrical face", 
    "Flawless complexion", "Smirking", "Glass skin", "Plump lips", "High cheekbones", 
    "Mona Lisa smile", "Mysterious look", "Sultry stare", "Defined brows", "Elegant nose", "A knowing glance", "Heart-shaped lips"
]
hair = [
    "Sleek ponytail", "Vibrant crimson hair", "Electric blue hair", "Undercut", "Messy bun", 
    "Long flowing hair", "Styled baby hairs", "Platinum blonde wolf cut", "Pastel pink bob", 
    "Jet black hime cut", "Braided space buns", "Wet look hair", "Face-framing tendrils", 
    "Two-tone hair (skunk stripe)", "Shaggy mullet", "Curtain bangs", "Intricate updo", "Glossy dark hair"
]
makeup = [
    "Smokey eye makeup", "Bold red lipstick", "Graphic eyeliner", "Glowing skin", "Contoured cheekbones", 
    "Dewy makeup look", "Glitter eyeshadow", "'Drunk blush' style", "Aegyo-sal makeup", "Gradient lips", 
    "Sharp winged liner", "Gemstone face accents", "Glossy eyelids", "Monochromatic makeup", 
    "Natural 'no-makeup' makeup", "Bleached brows", "Metallic lipstick"
]

# Category 4: The Setting (Brooklyn)
locations = [
"on a DUMBO street with the Manhattan Bridge in the background",
"on the Brooklyn Bridge walkway at dawn",
"in front of a massive graffiti mural in Bushwick",
"on a Williamsburg rooftop overlooking the skyline",
"in a gritty, rain-slicked Brooklyn alleyway",
"on a classic Brownstone stoop in Park Slope",
"under the BQE expressway with light trails from cars",
"on the Coney Island boardwalk at night",
"inside a renovated, industrial loft in Bushwick",
"on a graffiti-covered basketball court",
"in a dimly lit jazz club in Williamsburg",
"near Prospect Park's Boathouse",
"in a vintage record store filled with vinyls",
"on the steps of the Brooklyn Museum",
"in a bustling street market in Flatbush",
"inside an abandoned industrial warehouse",
"by the East River with city lights reflecting on the water",
"inside Jane's Carousel in DUMBO, lit up at night",
"walking the Williamsburg Bridge footpath, with Brooklyn behind you",
"picnicking on the Long Meadow in Prospect Park",
"on the Cherry Esplanade at the Brooklyn Botanic Garden during peak bloom",
"at Valentino Pier in Red Hook, looking out at the Statue of Liberty",
"inside a Polish bakery in Greenpoint, smelling freshly baked pastries",
"among the ruins of the old sugar refinery at Domino Park",
"on a bench on the Brooklyn Heights Promenade, watching the sunset over Manhattan",
"on a misty autumn day in Green-Wood Cemetery",
"paddling a pedal boat on the lake in Prospect Park",
"walking through the street art of the Bushwick Collective",
"eating a hot dog at Nathan's Famous amidst the sounds of Coney Island",
"on a bridge over the Gowanus Canal, surrounded by industrial decay",
"inside a crowded late-night bodega, under fluorescent lights",
"on the elevated platform of the Smith-9th Streets subway station, overlooking the borough",
"on a vibrant street in a Caribbean neighborhood in Crown Heights",
"amidst the fantastic Christmas light displays in Dyker Heights",
"ice skating at the LeFrak Center in Prospect Park",
"in the courtyard of Industry City, surrounded by repurposed industrial buildings",
"at the top of Sunset Park, enjoying a moment of quiet",
"on the boardwalk in Brighton Beach, surrounded by Russian conversation",
"at a warehouse party in a converted Bushwick art space",
"in a quiet backyard cafe in Carroll Gardens",
"biking down the Ocean Parkway bike path",
"at the Brooklyn Navy Yard, with new and old ships side-by-side",
"at the base of the Prison Ship Martyrs' Monument in Fort Greene Park",
"in front of the Brooklyn Academy of Music (BAM) theater",
"amidst the crowds and food stalls at Smorgasburg",
"on Vanderbilt Avenue in Prospect Heights, closed off for a weekend street fair",
"inside a classic barbershop in Bed-Stuy",
"at the busy intersection of Flatbush and Atlantic Avenues",
"inside a vintage subway car at the New York Transit Museum",
"strolling among the Victorian mansions of Ditmas Park",
"underneath the Wonder Wheel at Coney Island",
"on the docks in Sheepshead Bay, watching the fishing boats come in",
"in a secret, password-protected speakeasy bar",
"by the pool at McCarren Park",
"inside an independent bookstore in Williamsburg, surrounded by the smell of paper",
"on the cobblestone streets of Vinegar Hill, with the power station in the background",
"at a lively block party in East New York",
"on Pebble Beach in Brooklyn Bridge Park, listening to the water",
"inside a steamy, old-school pizzeria in Bensonhurst",
"at the Canarsie Pier, looking out over Jamaica Bay",
"hiking through the Salt Marsh at Marine Park",
"inside the Brooklyn Children's Museum, filled with sounds of joy",
"in a typical Boerum Hill backyard garden",
"at the Grand Army Plaza Greenmarket",
"watching an outdoor movie on the grass at McCarren Park in Williamsburg",
"on a rooftop farm in Bushwick",
"on the waterside patio of the giant Fairway Market in Red Hook",
"in a Hasidic Jewish neighborhood in South Williamsburg",
"waiting for a show to start in the ornate lobby of the Kings Theatre",
"browsing for antiques at the Brooklyn Flea",
"at Brooklyn Bowl in Gowanus, a combination bowling alley and music venue",
"exploring an abandoned military fort at Fort Tilden",
"in a secluded corner of Prospect Park known as The Vale of Cashmere",
"at the grand entrance of the Brooklyn Central Library",
"on a tree-lined street of brownstones in Cobble Hill",
"by the sea lion pool at the New York Aquarium",
"on the East River Ferry, traveling from DUMBO to Wall Street",
"in a late-night Polish diner in Greenpoint",
"at an improv comedy show in a basement venue",
"on the swaying Squibb Park Bridge in Brooklyn Bridge Park",
"during a vibrant Caribbean Carnival parade in Prospect Lefferts Gardens",
"on the shore promenade in Bay Ridge, looking at the Verrazzano-Narrows Bridge",
"in the library of the Center for Brooklyn History (formerly Brooklyn Historical Society)",
"waiting in line for brunch outside a busy Williamsburg restaurant",
"in the crowd outside the Barclays Center after a game",
"inside a West Indian bakery in Crown Heights",
"at the playgrounds on Pier 6 in Brooklyn Bridge Park",
"in a reclaimed furniture store in Williamsburg",
"at Bushwick Inlet Park at sunset",
"in the archway under the Manhattan Bridge, feeling the rumble of the train",
"at a private gallery opening, somewhere between Chelsea and Bushwick",
"admiring the preserved architecture in the Stuyvesant Heights Historic District",
"in a retro arcade bar, with 8-bit music in the background",
"in the botanic garden directly behind the Brooklyn Museum",
"inside a late-night music recording studio",
"spending a hot summer afternoon at the public pool in Red Hook's Valentino Park",
"in an indoor rock-climbing gym converted from an old factory",
"at the roller-skating rink on Pier 2 in Brooklyn Bridge Park",
"walking through an empty Financial District on a Sunday morning, heading towards Brooklyn",
"in a taqueria in Bushwick with murals on the walls",
"on the abandoned runways of Floyd Bennett Field"
]

footwear = [
    "Chunky boots", "High-top sneakers", "Stilettos", "Platform shoes", "Knee-high leather boots", 
    "Strappy heels", "Combat boots", "Designer trainers", "Ankle boots", "Mary Janes", 
    "Loafers", "Mules", "Over-the-knee boots", "Clear heels", "Tabi boots", "Wedge sneakers"
]

accessories = [
    "Layered chains", "Hoop earrings", "Designer sunglasses", "Beanie", "Choker", "Luxury handbag", 
    "Body chain", "Single statement earring", "Leather harness", "Beret", "Newsboy cap", 
    "Fingerless gloves", "Garter", "Arm cuffs", "Dainty necklaces", "Vintage watch", "Bandana", "Chain belt"
]

# Category 4: The Setting (Brooklyn)
locations = [
"on a DUMBO street with the Manhattan Bridge in the background",
"on the Brooklyn Bridge walkway at dawn",
"in front of a massive graffiti mural in Bushwick",
"on a Williamsburg rooftop overlooking the skyline",
"in a gritty, rain-slicked Brooklyn alleyway",
"on a classic Brownstone stoop in Park Slope",
"under the BQE expressway with light trails from cars",
"on the Coney Island boardwalk at night",
"inside a renovated, industrial loft in Bushwick",
"on a graffiti-covered basketball court",
"in a dimly lit jazz club in Williamsburg",
"near Prospect Park's Boathouse",
"in a vintage record store filled with vinyls",
"on the steps of the Brooklyn Museum",
"in a bustling street market in Flatbush",
"inside an abandoned industrial warehouse",
"by the East River with city lights reflecting on the water",
"inside Jane's Carousel in DUMBO, lit up at night",
"walking the Williamsburg Bridge footpath, with Brooklyn behind you",
"picnicking on the Long Meadow in Prospect Park",
"on the Cherry Esplanade at the Brooklyn Botanic Garden during peak bloom",
"at Valentino Pier in Red Hook, looking out at the Statue of Liberty",
"inside a Polish bakery in Greenpoint, smelling freshly baked pastries",
"among the ruins of the old sugar refinery at Domino Park",
"on a bench on the Brooklyn Heights Promenade, watching the sunset over Manhattan",
"on a misty autumn day in Green-Wood Cemetery",
"paddling a pedal boat on the lake in Prospect Park",
"walking through the street art of the Bushwick Collective",
"eating a hot dog at Nathan's Famous amidst the sounds of Coney Island",
"on a bridge over the Gowanus Canal, surrounded by industrial decay",
"inside a crowded late-night bodega, under fluorescent lights",
"on the elevated platform of the Smith-9th Streets subway station, overlooking the borough",
"on a vibrant street in a Caribbean neighborhood in Crown Heights",
"amidst the fantastic Christmas light displays in Dyker Heights",
"ice skating at the LeFrak Center in Prospect Park",
"in the courtyard of Industry City, surrounded by repurposed industrial buildings",
"at the top of Sunset Park, enjoying a moment of quiet",
"on the boardwalk in Brighton Beach, surrounded by Russian conversation",
"at a warehouse party in a converted Bushwick art space",
"in a quiet backyard cafe in Carroll Gardens",
"biking down the Ocean Parkway bike path",
"at the Brooklyn Navy Yard, with new and old ships side-by-side",
"at the base of the Prison Ship Martyrs' Monument in Fort Greene Park",
"in front of the Brooklyn Academy of Music (BAM) theater",
"amidst the crowds and food stalls at Smorgasburg",
"on Vanderbilt Avenue in Prospect Heights, closed off for a weekend street fair",
"inside a classic barbershop in Bed-Stuy",
"at the busy intersection of Flatbush and Atlantic Avenues",
"inside a vintage subway car at the New York Transit Museum",
"strolling among the Victorian mansions of Ditmas Park",
"underneath the Wonder Wheel at Coney Island",
"on the docks in Sheepshead Bay, watching the fishing boats come in",
"in a secret, password-protected speakeasy bar",
"by the pool at McCarren Park",
"inside an independent bookstore in Williamsburg, surrounded by the smell of paper",
"on the cobblestone streets of Vinegar Hill, with the power station in the background",
"at a lively block party in East New York",
"on Pebble Beach in Brooklyn Bridge Park, listening to the water",
"inside a steamy, old-school pizzeria in Bensonhurst",
"at the Canarsie Pier, looking out over Jamaica Bay",
"hiking through the Salt Marsh at Marine Park",
"inside the Brooklyn Children's Museum, filled with sounds of joy",
"in a typical Boerum Hill backyard garden",
"at the Grand Army Plaza Greenmarket",
"watching an outdoor movie on the grass at McCarren Park in Williamsburg",
"on a rooftop farm in Bushwick",
"on the waterside patio of the giant Fairway Market in Red Hook",
"in a Hasidic Jewish neighborhood in South Williamsburg",
"waiting for a show to start in the ornate lobby of the Kings Theatre",
"browsing for antiques at the Brooklyn Flea",
"at Brooklyn Bowl in Gowanus, a combination bowling alley and music venue",
"exploring an abandoned military fort at Fort Tilden",
"in a secluded corner of Prospect Park known as The Vale of Cashmere",
"at the grand entrance of the Brooklyn Central Library",
"on a tree-lined street of brownstones in Cobble Hill",
"by the sea lion pool at the New York Aquarium",
"on the East River Ferry, traveling from DUMBO to Wall Street",
"in a late-night Polish diner in Greenpoint",
"at an improv comedy show in a basement venue",
"on the swaying Squibb Park Bridge in Brooklyn Bridge Park",
"during a vibrant Caribbean Carnival parade in Prospect Lefferts Gardens",
"on the shore promenade in Bay Ridge, looking at the Verrazzano-Narrows Bridge",
"in the library of the Center for Brooklyn History",
"waiting in line for brunch outside a busy Williamsburg restaurant",
"in the crowd outside the Barclays Center after a game",
"inside a West Indian bakery in Crown Heights",
"at the playgrounds on Pier 6 in Brooklyn Bridge Park",
"in a reclaimed furniture store in Williamsburg",
"at Bushwick Inlet Park at sunset",
"in the archway under the Manhattan Bridge, feeling the rumble of the train",
"at a private gallery opening in a converted Bushwick loft",
"admiring the preserved architecture in the Stuyvesant Heights Historic District",
"in a retro arcade bar, with 8-bit music in the background",
"in the Japanese Hill-and-Pond Garden at the Brooklyn Botanic Garden",
"inside a late-night music recording studio",
"spending a hot summer afternoon at the public pool in Red Hook's Valentino Park",
"in an indoor rock-climbing gym converted from an old factory",
"at the roller-skating rink on Pier 2 in Brooklyn Bridge Park",
"walking through an empty Financial District on a Sunday morning, heading towards Brooklyn",
"in a taqueria in Bushwick with murals on the walls",
"on the abandoned runways of Floyd Bennett Field"
]

atmospheres = [
    "Urban grit", "Cityscape background", "Neon lights", "Moody atmosphere", "Cinematic", "Industrial setting", 
    "Raw and unfiltered", "Nostalgic and dreamlike", "Grungy and authentic", "High-energy and electric", 
    "Solitary and melancholic", "Hazy and mysterious", "Gritty realism", "Sophisticated urban vibe",
    "Vibrant street life", "Tranquility at night", "Retro cinematic feel" 
]

# Category 5: Photography & Artistic Style
shot_types = [
    "Full-body shot", "Dynamic pose", "Action shot", "Candid street style photo", "Close-up portrait", 
    "Editorial style photoshoot", "Low-angle shot emphasizing power", "High-angle shot", "Mid-shot", 
    "Over-the-shoulder shot", "Motion blur effect", "Dutch angle for unease", "Silhouette against the skyline", 
    "Profile shot", "Environmental portrait", "Black and white photo", "Wide-angle shot"
]
lighting = [
    "Dramatic lighting", "Hard shadows", "Lens flare", "Neon glow", "Soft diffused light", 
    "Golden hour lighting", "Blue hour lighting", "Rim lighting", "Split lighting", "Backlight", 
    "Chiaroscuro (strong light/dark contrast)", "Volumetric lighting", "Light leaks", "Bokeh background lights", 
    "Studio flash lighting on location", "Natural window light", "Muted tones", "Harsh direct flash"
]
quality = [
    "Photorealistic", "Hyper-detailed", "8K resolution", "Sharp focus", "Cinematic quality", 
    "Ultra realistic", "Insanely detailed", "Intricate details", "Professional photography", 
    "Hasselblad photo", "Shot on Portra 400 film", "Film grain", "Crystal clear", "High dynamic range (HDR)", 
    "Masterpiece quality", "Award-winning photography", "Unreal Engine 5 render", "Magazine cover quality"
]
styles = [
    "Fashion magazine aesthetic (like Vogue or Dazed)", "Music video still", "Movie poster style", "Street photography (like Vivian Maier)", 
    "Neo-noir film aesthetic", "Cyberpunk vibe", "Indie movie still", "90s fashion photography", 
    "Gritty documentary style", "High-fashion campaign", "Lo-fi aesthetic", "Surrealist photography",
    "Cinematic still from a Wong Kar-wai film", "Gritty realism", "Hyper-maximalism", "Urban fantasy"
]


def feifeigenerateprompt():
    """Generates a random, massively detailed prompt for an AI art generator."""

    # --- Let's build the prompt piece by piece ---

    # 1. Start with the core subject and their defining traits
    personality_trait1 = random.choice(vibes + menaces)
    personality_trait2 = random.choice(firecrackers + dime_pieces)
    subject_core = f"{personality_trait1} and {personality_trait2} {random.choice(subjects)}"

    # 2. Add specific appearance details
    appearance_details = f"with {random.choice(features)}, {random.choice(hair)}, and {random.choice(makeup)}"

    # 3. Describe the outfit
    outfit = f"wearing a {random.choice(clothing)}, {random.choice(footwear)}, accessorized with a {random.choice(accessories)}"

    # 4. Set the scene in Brooklyn
    setting = f"posing {random.choice(locations)}, embodying the {random.choice(atmospheres)} of the city"

    # 5. Define the photographic style
    photo_style = f"A {random.choice(shot_types)}, captured in a {random.choice(styles)}. The image features {random.choice(lighting)} and is {random.choice(quality)}."

    # --- Combine everything into a final prompt ---
    final_prompt = f"{subject_core}, {appearance_details}. She's {outfit}. {setting}. {photo_style}"

    return final_prompt
