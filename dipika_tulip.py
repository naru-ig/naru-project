import tkinter as tk
import math
import random

# Dipika Romantic Tulip — Windows / VS Code
# No external packages or music files are required.

APP_BG = "#070410"
PANEL_BG = "#120824"
GOLD = "#f59e0b"
PINK = "#fda4af"
HEART = "#fb7185"

PHRASES = [
    "I love you, Dipika ❤️",
    "আমি তোমাকে ভালোবাসি, দীপিকা ❤️",
    "मैं तुमसे प्यार करता हूँ, दीपिका ❤️",
    "میں تم سے پیار کرتا ہوں، دیپیکا ❤️",
    "愛してるよ、ディーピカー ❤️",
    "사랑해, 디피카 ❤️",
    "迪皮卡，我爱你 ❤️",
    "म तिमीलाई माया गर्छु, दीपिका ❤️",
    "মই তোমাক ভাল পাওঁ, দীপিকা ❤️",
    "தீபிகா, நான் உன்னை காதலிக்கிறேன் ❤️",
    "దీపికా, నేను నిన్ను ప్రేమిస్తున్నాను ❤️",
    "दीपिका, मी तुझ्यावर प्रेम करतो ❤️",
    "દીપિકા, હું તને પ્રેમ કરું છું ❤️",
    "ਦੀਪਿਕਾ, ਮੈਂ ਤੈਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ ❤️",
    "ดิพิกา ฉันรักคุณ ❤️",
    "Aku cinta kamu, Dipika ❤️",
    "Dipika, anh yêu em ❤️",
    "Je t’aime, Dipika ❤️",
    "Te amo, Dipika ❤️",
    "Ti amo, Dipika ❤️",
    "Ich liebe dich, Dipika ❤️",
    "Eu te amo, Dipika ❤️",
    "Я люблю тебя, Дипика ❤️",
    "Σ’ αγαπώ, Ντιπίκα ❤️",
    "Ik hou van jou, Dipika ❤️",
    "Kocham cię, Dipika ❤️",
    "Seni seviyorum, Dipika ❤️",
    "Jag älskar dig, Dipika ❤️",
    "أحبك يا ديبيكا ❤️",
    "אני אוהב אותך, דיפיקה ❤️",
    "دیپیکا، دوستت دارم ❤️",
    "Nakupenda, Dipika ❤️",
    "Mo nifẹ rẹ, Dipika ❤️",
    "Ngiyakuthanda, Dipika ❤️",
    "Waan ku jeclahay, Dipika ❤️",
    "ዲፒካ፣ እወድሻለሁ ❤️",
    "Ek is lief vir jou, Dipika ❤️",
    "Ina son ki, Dipika ❤️",
    "Tiako ianao, Dipika ❤️",
    "Mahal kita, Dipika ❤️",
    "Saya cinta padamu, Dipika ❤️",
    "ဒိပီကာ၊ မင်းကိုချစ်တယ် ❤️",
    "ឌីពីកា ខ្ញុំស្រឡាញ់អ្នក ❤️",
    "ດິພິກາ, ຂ້ອຍຮັກເຈົ້າ ❤️",
    "Би чамд хайртай, Дипика ❤️",
    "Мен сені сүйемін, Дипика ❤️",
    "Men seni sevaman, Dipika ❤️",
    "Ես քեզ սիրում եմ, Դիպիկա ❤️",
    "მიყვარხარ, დიპიკა ❤️",
    "Я тебе кохаю, Діпіка ❤️",
    "Te iubesc, Dipika ❤️",
    "Szeretlek, Dipika ❤️",
    "Miluji tě, Dipika ❤️",
    "Ľúbim ťa, Dipika ❤️",
    "Volim te, Dipika ❤️",
    "Волим те, Дипика ❤️",
    "Обичам те, Дипика ❤️",
    "Jeg elsker dig, Dipika ❤️",
    "Jeg elsker deg, Dipika ❤️",
    "Rakastan sinua, Dipika ❤️",
    "Ég elska þig, Dipika ❤️",
    "Tá grá agam duit, Dipika ❤️",
    "Rwy'n dy garu di, Dipika ❤️",
    "Maite zaitut, Dipika ❤️",
    "T'estimo, Dipika ❤️",
    "Aloha au iā ʻoe, Dipika ❤️",
    "E aroha ana ahau ki a koe, Dipika ❤️",
    "Ou te alofa ia te oe, Dipika ❤️",
    "Mi amas vin, Dipika ❤️",
]

def build_tulip_segments():
    """Create text strokes that form a stylized, layered tulip."""
    segments = []
    cx = 480
    stream = "   ✦   ".join(PHRASES) + "   ✦   "
    stream_index = 0

    def text_slice(length):
        nonlocal stream_index
        if length <= 0:
            return ""
        out = []
        remaining = length
        while remaining:
            take = min(remaining, len(stream) - stream_index)
            out.append(stream[stream_index:stream_index + take])
            stream_index = (stream_index + take) % len(stream)
            remaining -= take
        return "".join(out)

    # Stem and leaves
    for y in range(745, 439, -11):
        stem_x = cx + int(10 * math.sin((y - 440) / 55.0))
        stem_color = "#10b981" if (y // 11) % 2 == 0 else "#34d399"
        segments.append((stem_x, y, text_slice(6), stem_color, 9))

        if 495 <= y <= 715:
            p = (715 - y) / 220.0
            arch_offset = int(195 * math.sin(p * math.pi * 0.82))
            width = int(20 * math.sin(p * math.pi) * (1 - 0.25 * p))
            if width >= 3:
                leaf_color = "#059669" if p < 0.5 else "#10b981"
                segments.append((stem_x - arch_offset // 2 - 28, y,
                                 text_slice(width), leaf_color, 9))
                segments.append((stem_x + arch_offset // 2 + 28, y,
                                 text_slice(width), leaf_color, 9))

    # Blossom cup and crown
    for y in range(440, 134, -10):
        t = (440 - y) / 305.0
        if t < 0.68:
            cup_curve = math.sin((t / 0.68) * (math.pi / 2))
            half_width = int(215 * cup_curve)
            inner_chars = max(4, int(half_width * 1.15 / 6.2))
            segments.append((cx, y, text_slice(inner_chars), "#9d174d", 9))

            outer_chars = max(4, int(half_width * 0.92 / 6.0))
            left_color = "#fb7185" if (y // 10) % 2 == 0 else "#f43f5e"
            right_color = "#f43f5e" if (y // 10) % 2 == 0 else "#fda4af"
            offset = int(half_width * 0.46)
            segments.append((cx - offset, y, text_slice(outer_chars), left_color, 10))
            segments.append((cx + offset, y, text_slice(outer_chars), right_color, 10))
        else:
            tip_t = (t - 0.68) / 0.32
            if tip_t < 0.65:
                back_t = tip_t / 0.65
                back_chars = max(2, int(11 * (1 - back_t)))
                segments.append((cx - 66, y, text_slice(back_chars), "#be185d", 9))
                segments.append((cx + 66, y, text_slice(back_chars), "#be185d", 9))

            petal_width = int(68 * (1 - (tip_t ** 1.35)))
            char_len = max(2, int(petal_width * 2 / 6.4))
            if char_len >= 2:
                shift = int(128 + 14 * tip_t)
                segments.append((cx - shift, y, text_slice(char_len), "#fb7185", 10))
                segments.append((cx, y, text_slice(char_len + 2), "#e11d48", 10))
                segments.append((cx + shift, y, text_slice(char_len), "#fda4af", 10))
    return segments


class RomanticTulipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("For My Queen, Dipika ❤️🌷")
        self.root.geometry("960x850")
        self.root.resizable(False, False)
        self.root.configure(bg=APP_BG)

        self.canvas = tk.Canvas(
            root, width=960, height=850, bg=APP_BG, highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.started = False
        self.closed = False
        self.animation_after_id = None
        self.particles = []
        self.tulip_segments = build_tulip_segments()

        self._draw_background()
        self._create_particles()
        self._animate_particles()
        self._draw_header()
        self._create_intro()

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def _draw_background(self):
        self.canvas.create_oval(180, 90, 780, 690, fill="#0f0722", outline="")
        self.canvas.create_oval(260, 150, 700, 590, fill="#160a2c", outline="")
        self.canvas.create_rectangle(18, 18, 942, 832, outline="#3b1d54", width=1)
        self.canvas.create_rectangle(24, 24, 936, 826, outline=GOLD, width=1)

    def _create_particles(self):
        symbols = ["✨", "❤️", "💖", "🌸", "✦", "🌷"]
        colors = ["#fb7185", "#fcd34d", "#f43f5e", "#fda4af"]
        for _ in range(36):
            x = random.randint(40, 920)
            y = random.randint(80, 800)
            symbol = random.choice(symbols)
            color = random.choice(colors)
            item = self.canvas.create_text(
                x, y, text=symbol, fill=color,
                font=("Segoe UI Emoji", random.randint(9, 15))
            )
            self.particles.append([
                item, random.uniform(0, 6.28),
                random.uniform(0.6, 1.4), x, y
            ])

    def _animate_particles(self):
        if self.closed:
            return
        for particle in self.particles:
            item, phase, speed, origin_x, y = particle
            phase += 0.06
            y -= speed
            if y < 75:
                y = 810
                origin_x = random.randint(50, 910)
            x = origin_x + math.sin(phase) * 14
            self.canvas.coords(item, x, y)
            particle[1] = phase
            particle[3] = origin_x
            particle[4] = y
        self.root.after(55, self._animate_particles)

    def _draw_header(self):
        self.canvas.create_text(
            480, 54,
            text="✨ 🌷  A Royal Tulip of 69 Languages for Dipika  🌷 ✨",
            fill="#fecdd3", font=("Georgia", 19, "bold")
        )
        self.ticker_label = self.canvas.create_text(
            480, 88,
            text="Every petal whispers your name across the world...",
            fill="#fcd34d", font=("Segoe UI", 12, "bold"),
            width=850
        )

    def _create_intro(self):
        self.intro_items = []
        self.intro_items.append(self.canvas.create_rectangle(
            250, 290, 710, 540, fill=PANEL_BG, outline=GOLD, width=2
        ))
        self.intro_items.append(self.canvas.create_text(
            480, 355, text="👑  For My Queen, Dipika  👑",
            fill="#fef08a", font=("Georgia", 22, "bold")
        ))
        self.intro_items.append(self.canvas.create_text(
            480, 400, text="69 Languages of Love Woven Into One Blooming Tulip",
            fill=PINK, font=("Segoe UI", 11)
        ))
        self.start_button = tk.Button(
            self.root,
            text="💌  Click to Bloom Your Tulip, Dipika ❤️",
            command=self.begin_experience,
            bg="#e11d48", fg="#ffffff",
            activebackground="#be123c", activeforeground="#fef08a",
            font=("Segoe UI", 13, "bold"), relief="flat",
            padx=24, pady=10, cursor="hand2"
        )
        self.start_button_window = self.canvas.create_window(
            480, 468, window=self.start_button
        )

    def begin_experience(self):
        if self.started:
            return
        self.started = True
        for item in self.intro_items:
            self.canvas.delete(item)
        self.canvas.delete(self.start_button_window)
        self.start_button.destroy()
        self.draw_bloom_step(0)

    def draw_bloom_step(self, index):
        if self.closed:
            return
        if index < len(self.tulip_segments):
            end = min(index + 3, len(self.tulip_segments))
            for x, y, text_slice, color, size in self.tulip_segments[index:end]:
                self.canvas.create_text(
                    x, y, text=text_slice, fill=color,
                    font=("Segoe UI", size, "bold"), anchor="center"
                )

            lang_index = min(
                int((end / len(self.tulip_segments)) * (len(PHRASES) - 1)),
                len(PHRASES) - 1
            )
            self.canvas.itemconfig(
                self.ticker_label,
                text=f"🌍 Language {lang_index + 1} of {len(PHRASES)}: "
                     f"{PHRASES[lang_index]}"
            )
            self.animation_after_id = self.root.after(
                100, self.draw_bloom_step, end
            )
        else:
            self.canvas.itemconfig(
                self.ticker_label,
                text=f"💖 All {len(PHRASES)} Languages Bloomed for My Queen, Dipika 💖"
            )
            self.canvas.create_rectangle(
                210, 762, 750, 808, fill="#190b2e", outline=GOLD, width=2
            )
            self.canvas.create_text(
                480, 785, text="👑  this is only my queen, Dipika  ❤️",
                fill="#fde047", font=("Georgia", 18, "bold italic")
            )
            self.root.after(700, self.create_royal_popup)

    def create_royal_popup(self):
        if self.closed:
            return
        popup = tk.Toplevel(self.root)
        popup.title("My Queen, Dipika 👑")
        popup.geometry("540x310")
        popup.configure(bg="#090514")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        self.root.update_idletasks()
        x = self.root.winfo_x() + (960 - 540) // 2
        y = self.root.winfo_y() + (850 - 310) // 2
        popup.geometry(f"540x310+{max(0, x)}+{max(0, y)}")

        canvas = tk.Canvas(
            popup, width=540, height=310,
            bg="#090514", highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(14, 14, 526, 296, outline=GOLD, width=2)
        canvas.create_rectangle(22, 22, 518, 288, outline=HEART, width=1)
        canvas.create_text(
            270, 62, text="✨  👑  ✨", fill="#fcd34d",
            font=("Segoe UI Emoji", 24, "bold")
        )
        canvas.create_text(
            270, 125, text="“ this is only my queen, Dipika ”",
            fill="#fff1f2", font=("Georgia", 20, "bold italic")
        )
        canvas.create_text(
            270, 175,
            text="মই তোমাক ভাল পাওঁ •  মোক বিয়া কৰা  •  দীপিকা ❤️",
            fill=PINK, font=("Segoe UI", 10, "bold"), width=490
        )
        close_button = tk.Button(
            popup, text="❤️  Forever My Queen, Dipika  ❤️",
            command=popup.destroy, bg="#e11d48", fg="#ffffff",
            activebackground="#be123c", activeforeground="#fef08a",
            font=("Segoe UI", 11, "bold"), relief="flat",
            padx=22, pady=8, cursor="hand2"
        )
        canvas.create_window(270, 238, window=close_button)

    def close_app(self):
        self.closed = True
        try:
            if self.animation_after_id is not None:
                self.root.after_cancel(self.animation_after_id)
        except tk.TclError:
            pass
        self.root.destroy()


def main():
    root = tk.Tk()
    RomanticTulipApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
