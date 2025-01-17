from moviepy import *
import random



def video_main():
    # Load the top image and set duration
    top_image = ImageClip("./images/top-image.jpg").with_duration(5).resized(width=500).with_position(("center",100))

    # Set font and create a base color layer
    font = "font.ttf"
    base_layer = ColorClip((1080, 1920), color=(26, 26, 29)).with_duration(5)

    bg = VideoFileClip('bg.mp4')
    bg = bg.without_audio()
    f = open('voice.txt')
    text = f.read().strip()

    text_clip = TextClip(text=text, font=font, font_size=60, color='white')
    text_clip = text_clip.with_position(('center',700)).with_duration(5)

    # Load grid images and set durations
    image1 = ImageClip("./images/image1.jpg").with_duration(5).resized(width=350).with_effects([vfx.Margin(50,opacity=0)]) 
    image2 = ImageClip("./images/image2.jpg").with_duration(5).resized(width=350).with_effects([vfx.Margin(50,opacity=0)]) 
    image3 = ImageClip("./images/image3.jpg").with_duration(5).resized(width=350).with_effects([vfx.Margin(50,opacity=0)]) 
    image4 = ImageClip("./images/image4.jpg").with_duration(5).resized(width=350).with_effects([vfx.Margin(50,opacity=0)]) 

    # Create a timer clip
    timer_clip1 = TextClip(text="5", font=font, font_size=100, color='white').with_duration(1)
    timer_clip2 = TextClip(text="4", font=font, font_size=100, color='white').with_duration(1)
    timer_clip3 = TextClip(text="3", font=font, font_size=100, color='white').with_duration(1)
    timer_clip4 = TextClip(text="2", font=font, font_size=100, color='white').with_duration(1)
    timer_clip5 = TextClip(text="1", font=font, font_size=100, color='white').with_duration(1)

    timer_clip = concatenate_videoclips([timer_clip1,timer_clip2,timer_clip3,timer_clip4,timer_clip5]).with_position(("center",1225))


    array = [
        [image1, image2],
        [image4, image3],
    ]
    random.shuffle(array)
    array_clip = clips_array(array).with_position(("center",800))

    fname = f'./audio/audio.wav'
    audioclip = AudioFileClip(fname).with_volume_scaled(2)

    prev_t = 0
    def zoom_in(t):
        global prev_t
        if t < 0.5:
            prev_t = t + 0.4
            return t + 0.4
        else:
            return prev_t

    initial_clip = CompositeVideoClip([
        bg.subclipped(0,audioclip.duration),
        text_clip.with_duration(audioclip.duration).with_effects([vfx.Resize(zoom_in)]),
        top_image.with_duration(audioclip.duration),
        array_clip.with_duration(audioclip.duration)
    ]).with_audio(audioclip)


    count_down = AudioFileClip("./audio/count2.mp3") 

    # Trim the audio to the first 5 seconds
    count_down = count_down.subclipped(0, 5) 

    main_clip = CompositeVideoClip([
        bg.subclipped(0,5),
        text_clip,
        top_image,
        array_clip,
        timer_clip,
    ]).with_audio(count_down)




    celeb = AudioFileClip("./audio/celeb.mp3").with_volume_scaled(0.5)

    celeb = celeb.subclipped(0, 5) 

    # Show The Answer Image
    answer_image = ImageClip("./images/image4.jpg").with_duration(5).resized(width=700).with_position("center")
    answer_image = answer_image.with_effects([vfx.Resize(zoom_in)])
    text_clip = TextClip(text="Subscribe If You Are \n           CORRECT", font=font, font_size=60, color='white')
    text_clip = text_clip.with_position(('center',1500)).with_duration(5)

    answer_clip = CompositeVideoClip([
        bg.subclipped(0,5),
        answer_image,
        text_clip
    ]).with_audio(celeb)


    # Concatenate with the selected image
    final_clip = concatenate_videoclips([initial_clip,main_clip, answer_clip])

    # Render the video
    final_clip.write_videofile("output.mp4", fps=30)