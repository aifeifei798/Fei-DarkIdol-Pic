import random

# --- V3.0 - Japanese "Kawaii" Idol Edition ---
# 主题: 有活力, 吸引人, 萌萌哒, 甜甜哒 (Energetic, Captivating, Cute, Sweet)

# Category 1: 偶像的氛围与个性 (The Vibe & Personality)
cute_vibes = [
    "Adorable", "Sweet", "Charming", "Angelic", "Innocent", "Pure", "Lovely",
    "Heartwarming", "Endearing", "Gentle", "A ray of sunshine", "Moe", "Precious",
    "Girly", "Dreamy", "Captivating", "Attractive", "Enchanting", "Delightful", "Sweet-natured"
]
energetic_vibes = [
    "Energetic", "Bubbly", "Lively", "Spirited", "Cheerful", "Playful", "Vivacious",
    "Dynamic", "Upbeat", "Genki", "Radiant", "Sparkling", "Full of life", "Active",
    "Effervescent", "Enthusiastic", "Gleeful", "Animated", "Youthful", "Bright"
]
idol_qualities = [
    "The 'center' idol", "A rookie idol full of hope", "The lead vocalist", "A charismatic dancer",
    "A popular J-pop idol", "An underground idol (Chika idol)", "A rising star",
    "A beloved Japanese pop star", "A 'kawaii' fashion model", "An Akihabara idol",
    "A member of a famous idol group", "A solo idol artist", "An angelic idol"
]

# Category 2: 外貌与造型 (Appearance & Style)

# --- 可爱的服装、配饰和泳装 (Cute Clothing, Accessories & Swimwear) ---
clothing = [
    "a frilly pink and white idol stage costume with a matching bow",
    "a Japanese school uniform (seifuku) with a cute red ribbon",
    "a pastel-colored 'kawaii' style dress covered in lace",
    "a sailor-style outfit (sailor fuku) with a pleated skirt",
    "a 'Liz Lisa' style floral print dress with ruffles",
    "a layered outfit with a Peter Pan collar blouse and a jumper skirt",
    "a sweet lolita dress with a bonnet",
    "a maid costume from an Akihabara maid cafe",
    "a cute animal-themed kigurumi (onesie)",
    "a casual outfit with a graphic t-shirt and a tennis skirt",
    "a cozy, oversized pastel sweater with a short skirt",
    "a light, airy yukata worn for a summer festival",
    "a simple white dress, giving off a pure and innocent vibe",
    "a gingham pattern sundress perfect for a picnic",
    "an outfit inspired by a magical girl anime character",
    # --- 泳装 (Swimwear) ---
    "a cute pastel-colored bikini with frills",
    "a high-waisted retro bikini with a cherry print",
    "a classic school swimsuit (suku-mizu)",
    "a one-piece swimsuit with a big ribbon on the chest",
    "a floral print bikini with a matching sarong",
    "a pink and white striped bikini",
    "a crochet, bohemian-style bikini for a beach photoshoot",
    "a halter top bikini that ties around the neck",
    "a gingham pattern bikini"
]
footwear = [
    "Mary Janes with white lace-trimmed socks",
    "cute sneakers with colorful laces and charms",
    "platform shoes in a pastel color",
    "classic school loafers",
    "strappy sandals with small bows",
    "ugg boots for a casual look",
    "white ankle boots"
]
accessories = [
    "a large ribbon in her hair",
    "a cute character plushie held in her arms",
    "a star-shaped magic wand prop",
    "a cat ear headband",
    "a small, cute backpack with pins",
    "white thigh-high stockings",
    "a delicate heart-shaped necklace",
    "colorful beaded bracelets",
    "a flower crown",
    "a small, decorative beret"
]

# --- 可爱的外貌特征 (Cute Features) ---
features = [
    "Big, sparkling doe-eyes", "A bright, genuine smile", "A cute button nose", "Round, rosy cheeks",
    "A youthful face", "Soft, clear skin", "A slightly surprised, innocent expression",
    "Plump, glossy lips", "A charming and sweet look", "A gentle gaze", "A cheerful expression"
]
hair = [
    "Twin-tails (pigtails) tied with ribbons",
    "A fluffy short bob with straight-cut bangs",
    "Long, wavy pastel pink hair",
    "A classic 'hime cut'",
    "A cute side ponytail",
    "Fluffy, light brown hair with a slight curl",
    "Braided hair decorated with small flowers",
    "Jet black straight hair with full bangs ('patsun')",
    "Pastel blue or lavender colored hair",
    "A messy bun with cute, face-framing strands"
]
makeup = [
    "a natural, youthful makeup look",
    "a generous amount of pink blush on the cheeks ('Igari' style)",
    "glossy pink lips",
    "subtle, sparkling glitter on the eyelids",
    "cute puppy-dog eyeliner to make the eyes look rounder",
    "'Aegyo-sal' (puffy under-eye) makeup to emphasize cuteness",
    "a touch of highlighter for a dewy skin look",
    "a very light, natural foundation",
    "soft, straight eyebrows"
]
poses = [
    "making a heart sign with her hands",
    "winking and giving a peace sign",
    "puffing her cheeks in a playful way",
    "holding her hands to her face in a surprised 'moe' gesture",
    "a cute head tilt with a curious expression",
    "doing a 'Nyan' (cat) pose with her hands as paws",
    "a shy smile while looking slightly away from the camera",
    "spinning in her dress",
    "holding a microphone and singing with passion",
    "jumping in the air with a joyful expression"
]

# Category 3: 场景与氛围 (Setting & Atmosphere)
locations = [
    "on a bright, colorful idol stage during a live performance",
    "in a colorful Harajuku creperie, holding a sweet crepe",
    "at Sanrio Puroland, surrounded by cute characters",
    "inside a Japanese photo booth (purikura) with cute stickers and filters",
    "in a sunlit park under blooming cherry blossom trees",
    "in Akihabara, in front of a wall of gachapon machines",
    "in a themed 'kawaii' cafe with pastel decorations",
    "on a sandy beach during a summer photoshoot",
    "in a high school classroom set, for a nostalgic feel",
    "at a traditional summer festival (matsuri), holding a candy apple",
    "in a bright, clean, modern recording studio",
    "on a pedestrian bridge in Shibuya, smiling at the camera",
    "in a field of sunflowers",
    "in a cozy, cute bedroom decorated with plushies",
    "at an amusement park, riding a merry-go-round"
]
atmospheres = [
    "A bright and cheerful atmosphere", "A dreamy and sweet aesthetic", "A bubbly and energetic vibe",
    "A feeling of pure happiness and innocence", "A pastel-colored world", "A 'kawaii' overload",
    "A warm and inviting feeling", "A sense of youthful optimism", "A lighthearted and fun mood",
    "A magical and enchanting setting"
]

# Category 4: 摄影与艺术风格 (Photography & Artistic Style)
shot_types = [
    "Full-body shot showcasing her costume", "Close-up portrait focusing on her cute expression",
    "A dynamic action shot of her dancing", "A candid, behind-the-scenes style photo",
    "A mid-shot from the waist up", "A low-angle shot making her look energetic",
    "A high-angle shot emphasizing her cuteness", "An environmental portrait showing the location",
    "A shot with motion blur to convey energy", "A soft-focus, dreamy shot"
]
lighting = [
    "Soft, diffused lighting that's very flattering", "Bright, high-key lighting", "Golden hour sunlight",
    "Colorful stage lighting with spotlights", "Lens flare for a dreamy effect",
    "Natural window light in a cozy room", "Bokeh background of city lights",
    "A gentle backlight creating a halo effect"
]
quality = [
    "Photorealistic", "Hyper-detailed", "8K resolution", "Sharp focus", "Cinematic quality",
    "Ultra realistic", "Insanely detailed", "Crystal clear", "High dynamic range (HDR)",
    "Masterpiece quality", "Professional idol photography", "Magazine cover quality"
]
styles = [
    "An idol photobook (shashinshū) style", "A J-pop music video still", "A promotional poster for an idol group",
    "A page from a Japanese teen fashion magazine like 'Seventeen'", "A candid 'off-shot' photo style",
    "A cheerful and bright commercial advertisement", "A dreamy, cinematic movie still",
    "A clean, minimalist studio photoshoot", "A 'lomography' film photo aesthetic with light leaks"
]


def feifeigenerateprompt():
    """Generates a random, detailed prompt for an AI art generator with a Japanese 'Kawaii' Idol theme."""

    # --- Let's build the prompt piece by piece ---

    # 1. 核心主语与个性 (Core subject and personality)
    personality_trait1 = random.choice(cute_vibes)
    personality_trait2 = random.choice(energetic_vibes)
    subject_core = f"{personality_trait1} and {personality_trait2} {random.choice(idol_qualities)}"

    # 2. 具体外貌细节 (Specific appearance details)
    appearance_details = f"with {random.choice(features)}, {random.choice(hair)}, and {random.choice(makeup)}"

    # 3. 描述服装和姿势 (Describe the outfit and pose)
    outfit = f"wearing {random.choice(clothing)}, and accessorized with {random.choice(accessories)}"
    pose = f"She is {random.choice(poses)}"

    # 4. 设定场景 (Set the scene)
    setting = f"{random.choice(locations)}, filled with {random.choice(atmospheres)}"

    # 5. 定义摄影风格 (Define the photographic style)
    photo_style = f"{random.choice(shot_types)}, captured in the style of {random.choice(styles)}. The image features {random.choice(lighting)} and is {random.choice(quality)}."

    # --- 组合所有内容 (Combine everything into a final prompt) ---
    final_prompt = f"{subject_core}, {appearance_details}. {pose}, {outfit}. The scene is {setting}. {photo_style}"

    return final_prompt

# --- 使用示例 (Example Usage) ---
# new_idol_prompt = feifeigenerateprompt()
# print(new_idol_prompt)