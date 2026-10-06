import random
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from googletrans import Translator

DURATION = 5
SAMPLE_RATE = 44100

aciertos = 0
inaciertos = 0

recognized = {

    "facil": ["cat", "dog", "apple", "milk", "sun"],

    "medio": ["banana", "school", "friend", "window", "yellow"],

    "dificil": ["technology", "university", "information", "pronunciation", "imagination"],

}

translator = Translator()

while True:

    if aciertos == 0:

        palabra = random.choice(recognized["facil"])

        print(f"Palabra a pronunciar: {palabra}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 1:

        palabra1 = random.choice(recognized["facil"])

        while palabra1 == palabra:

            palabra1 = random.choice(recognized["facil"])

        print(f"Palabra a pronunciar: {palabra1}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra1:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 2:

        palabra2 = random.choice(recognized["medio"])

        print(f"Palabra a pronunciar: {palabra2}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra2:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 3:

        palabra3 = random.choice(recognized["medio"])

        while palabra3 == palabra2:

            palabra3 = random.choice(recognized["medio"])

        print(f"Palabra a pronunciar: {palabra3}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra3:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 4:

        palabra4 = random.choice(recognized["dificil"])

        print(f"Palabra a pronunciar: {palabra4}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra4:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 5:

        palabra5 = random.choice(recognized["dificil"])

        while palabra5 == palabra4:

            palabra5 = random.choice(recognized["dificil"])

        print(f"Palabra a pronunciar: {palabra5}")

        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        wav.write("output.wav", SAMPLE_RATE, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:

            texto = recognizer.recognize_google(audio, language="en")

            texto = texto.lower()

            print(f"Dijiste: {texto}")

            try:

                traduccion = translator.translate(texto, dest="es")

                if traduccion is not None:

                    print(f"En español: {traduccion.text}")

                else:

                    print("No se pudo traducir la palabra.")

            except Exception:

                print("No se pudo traducir la palabra.")

            if texto == palabra5:

                print("¡Correcto!")

                aciertos += 1

            else:

                print("¡Incorrecto!")

                inaciertos += 1

        except sr.UnknownValueError:

            print("No se pudo reconocer la voz.")

            inaciertos += 1

        except sr.RequestError:

            print("Error con el reconocimiento de voz.")

            inaciertos += 1

    elif aciertos == 6:

        print("¡Felicidades! Has completado el juego.")

        print(f"Total de aciertos: {aciertos}")

        print(f"Total de inaciertos: {inaciertos}")

        break