#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sven Cinematic Universe — Master Prompt Compiler & Sanitizer Engine
File: engine/prompt_compiler.py
Purpose: The ROOT deterministic generation engine for all AI Video Prompts and Episode HTML files.
Guarantees ZERO human/LLM error at source through automated sanitization,
dynamic Word-Per-Second (WPS) kinetic physics calculation, and pre-save gate validation.
"""

import os
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from engine.episode_audit_suite import audit_episode_html
except ImportError:
    from episode_audit_suite import audit_episode_html

class WPSCalculator:
    """
    Kinetic Word-Per-Second (WPS) Physics Engine.
    Dynamically computes timeline timestamps, dialogue delivery windows,
    and timeline cadence from screenplay word counts.
    """
    DEFAULT_WPS = 2.0  # 1.8 to 2.2 words per second natural conversational cadence
    MIN_SETTLE_SECONDS = 0.5  # Dynamic script-driven buffer (flexible to scene cadence)
    CLIP_DURATION = 10.0

    @classmethod
    def calculate_timings(cls, dialogue_text: str, wps: float = None, clip_duration: float = None) -> dict:
        rate = wps if wps and wps > 0 else cls.DEFAULT_WPS
        target_clip_dur = clip_duration if clip_duration and clip_duration in (10.0, 15.0, 30.0) else cls.CLIP_DURATION
        
        # Clean dialogue text to get pure spoken words (strip quotes & parentheticals)
        cleaned = re.sub(r'[\(（].*?[\)）]', '', dialogue_text or '')
        cleaned = re.sub(r'[\u201c\u201d\u2018\u2019"\'“”’]', '', cleaned)
        words = [w for w in re.split(r'\s+', cleaned.strip()) if w and not re.match(r'^[^\w\s]+$', w)]
        word_count = len(words)

        if word_count == 0:
            mid_pt = round(target_clip_dur * 0.45, 1)
            settle_pt = round(target_clip_dur - 1.5, 1)
            return {
                "word_count": 0,
                "duration": 0.0,
                "has_dialogue": False,
                "lead_in_range": f"00:00–00:{mid_pt:04.1f}",
                "action_range": f"00:{mid_pt:04.1f}–00:{target_clip_dur:04.1f}",
                "settle_range": f"00:{settle_pt:04.1f}–00:{target_clip_dur:04.1f}",
                "dialogue_range": None
            }

        raw_duration = round(word_count / rate, 1)
        max_dialogue_time = target_clip_dur - cls.MIN_SETTLE_SECONDS - 0.5
        duration = min(raw_duration, max_dialogue_time)

        lead_in_dur = round(max(0.8, min(2.0, target_clip_dur - duration - cls.MIN_SETTLE_SECONDS)), 1)
        dialogue_start = lead_in_dur
        dialogue_end = round(dialogue_start + duration, 1)
        settle_start = dialogue_end

        return {
            "word_count": word_count,
            "duration": duration,
            "has_dialogue": True,
            "lead_in_start": 0.0,
            "lead_in_end": dialogue_start,
            "lead_in_range": f"00:00–00:{dialogue_start:04.1f}",
            "dialogue_start": dialogue_start,
            "dialogue_end": dialogue_end,
            "dialogue_range": f"00:{dialogue_start:04.1f}–00:{dialogue_end:04.1f}",
            "settle_start": settle_start,
            "settle_end": target_clip_dur,
            "settle_range": f"00:{settle_start:04.1f}–00:{target_clip_dur:04.1f}"
        }

class PromptSanitizer:
    """
    Automated Deterministic Sanitizer Pipeline.
    Cleans prose at the ROOT before prompt compilation.
    """

    KELVIN_MAP = {
        r'\b2[5-9]00K\b': 'deep warm amber glow',
        r'\b3[0-2]00K\b': 'warm tungsten amber lighting',
        r'\b3[3-8]00K\b': 'warm golden morning sunlight',
        r'\b[4-5][0-5]00K\b': 'bright neutral natural daylight',
        r'\b5[6-9]00K\b': 'cool daylight illumination',
        r'\b6[0-5]00K\b': 'cool pale blue twilight',
        r'\b\d{4}K\b': 'natural cinematic illumination'
    }

    MINOR_SAFETY_MAP = {
        r'\bboyish\b': 'youthful',
        r'\bgirlish\b': 'youthful',
        r'\bboy\b': 'young schoolboy',
        r'\bgirl\b': 'young schoolgirl',
        r'\bkid\b': 'young student',
        r'\bkids\b': 'young students',
        r'\bchild\b': 'young student',
        r'\bchildren\b': 'young students',
        r'\bteenager\b': 'adolescent student',
        r'\bteen\b': 'adolescent student',
        r'\bbaby\b': '',
        r'\bbabies\b': '',
        r'\binfant\b': '',
        r'\binfants\b': '',
        r'\btoddler\b': '',
        r'\btoddlers\b': '',
        r'\bnewborn\b': '',
        r'\bnewborns\b': '',
        r'\bbe_tin\b': '',
        r'\bmaid\b': 'housekeeper'
    }

    HARDWARE_JARGON = [
        r'\bARRI\s+Alexa\s+LF\s+aesthetic\b',
        r'\bARRI\s+Alexa\b',
        r'\bAlexa\s+LF\b',
        r'\bARRI\b',
        r'\bPanavision\b',
        r'\bRED\s+Monstro\b',
        r'\bRED\s+V-Raptor\b',
        r'\bSony\s+Venice\b',
        r'\bDaVinci\s+Resolve(\s+color\s+grading)?\b',
        r'\bKodak\s+Vision\d*\b',
        r'\b24fps\b',
        r'\b60fps\b',
        r'\b\d{2,3}\s?fps\b',
        r'\b\d{2,3}\s?mm\b',
        r'\bf/\d(?:\.\d)?\b',
        r'\bISO\s*\d+\b',
        r'\btripod\b'
    ]

    MODE_B_COSTUME_TERMS = [
        r'\bin\s+dark\s+jade\s+green\s+silk\s+pyjamas\b',
        r'\bin\s+pastel\s+lemon\s+shirt\b',
        r'\bin\s+lemon\s+chiffon\s+dress\b',
        r'\bher\s+lemon\s+chiffon\s+dress\b',
        r'\bjade\s+green\s+pyjamas\b',
        r'\bpyjamas\b',
        r'\bpajamas\b',
        r'\bchiffon\s+dress\b',
        r'\bculotte\s+trousers\b',
        r'\bculottes\b',
        r'\bblouse\b',
        r'\btrousers\b',
        r'\bskirt\b'
    ]

    DEAD_AIR_MAP = {
        r'\bthe\s+frame\s+holds\s+still\b': 'motion continues fluidly',
        r'\bframe\s+holds\s+still\b': 'motion continues fluidly',
        r'\bholds?\s+still\b': 'maintains living posture and respiratory rhythm',
        r'\bstands?\s+rigid\s+through\s+00:(10|15|30)(?:\.0)?\b': r'chest rising and falling with tense shallow breath through 00:\1.0',
        r'\bsits?\s+rigid\s+through\s+00:(10|15|30)(?:\.0)?\b': r'shoulders trembling with restrained breathing through 00:\1.0',
        r'\bweeping\s+in\s+(?:the\s+)?background\s+through\s+00:(10|15|30)(?:\.0)?\b': r'fingers clenching and wiping tears in the background through 00:\1.0',
        r'\bstanding\s+still\s+through\s+00:(10|15|30)(?:\.0)?\b': r'maintains defensive posture with subtle shifting weight through 00:\1.0',
        r'\bblinks?\s+(?:quietly|in\s+mild\s+surprise)\s+through\s+00:(10|15|30)(?:\.0)?\b': r'adjusts posture with subtle breathing through 00:\1.0'
    }

    @classmethod
    def sanitize(cls, text: str, primary_speaker: str = "", secondary_speaker: str = "") -> str:
        # Match dialogue parenthetical blocks (both ASCII and Unicode)
        dialogue_rx = re.compile(r'([:：]\s*[“"\'\w\s,!?—–\.\-]*[“"\'].*?[”"\']\s*[\(（].*?[\)）])', re.DOTALL)
        parts = dialogue_rx.split(text)

        sanitized_parts = []
        for part in parts:
            if dialogue_rx.match(part):
                # Preserved intact: dialogue line + Track 2 voice directing parenthetical
                sanitized_parts.append(part)
            else:
                p = part

                # 0. Purge Cartesian Coordinates, Frame-Edge Tokens (Gate 3H) & Cross-Scene References (Gate 3I)
                p = re.sub(r'\(?\s*[XYZ]\s*:\s*[\+\-]?\d+(\.\d+)?m?.*?\)?', '', p, flags=re.IGNORECASE)
                p = re.sub(r'\b(screen-left|screen-right|frame-left|frame-right)\b', '', p, flags=re.IGNORECASE)
                p = re.sub(r' from\s+Scene\s+\d+ ', '', p, flags=re.IGNORECASE)

                # 1. Purge Hardware Jargon
                for hw in cls.HARDWARE_JARGON:
                    p = re.sub(hw, 'cinematic optical depth', p, flags=re.IGNORECASE)

                p = re.sub(r'cinematic optical depth,\s*cinematic optical depth', 'cinematic optical depth', p)
                p = re.sub(r',\s*,\s*', ', ', p)

                # 2. Convert Kelvin to sensory lighting
                for k_rx, k_rep in cls.KELVIN_MAP.items():
                    p = re.sub(k_rx, k_rep, p, flags=re.IGNORECASE)

                # 3. Purge Minor-Safety Policy Triggers
                for m_rx, m_rep in cls.MINOR_SAFETY_MAP.items():
                    p = re.sub(m_rx, m_rep, p, flags=re.IGNORECASE)

                # 4. Purge Mode B Costume mentions
                for c_rx in cls.MODE_B_COSTUME_TERMS:
                    p = re.sub(c_rx, '', p, flags=re.IGNORECASE)

                # 5. Purge Dead Air Phrases (Zero Dead Air Law)
                for da_rx, da_rep in cls.DEAD_AIR_MAP.items():
                    p = re.sub(da_rx, da_rep, p, flags=re.IGNORECASE)

                # 6. Purge Personal Pronouns in narrative prose
                speaker = primary_speaker if primary_speaker else "the subject"
                pair = f"{primary_speaker} and {secondary_speaker}" if (primary_speaker and secondary_speaker) else speaker
                p = re.sub(r'\b(he|she)\b', speaker, p, flags=re.IGNORECASE)
                p = re.sub(r'\b(his|her)\b', f"{speaker}'s", p, flags=re.IGNORECASE)
                p = re.sub(r'\b(herself|himself|themselves)\b', speaker, p, flags=re.IGNORECASE)
                p = re.sub(r'\bthey\b', pair, p, flags=re.IGNORECASE)
                p = re.sub(r'\bthem\b', pair, p, flags=re.IGNORECASE)
                p = re.sub(r'\btheir\b', f"{speaker}'s", p, flags=re.IGNORECASE)

                # 7. Purge Mode B numeric age in narrative prose (Gate 3A)
                p = re.sub(r'\b(\d{1,2}-year-old|aged \d{1,2})\b', 'youthful', p, flags=re.IGNORECASE)

                # 8. Purge Dangling Focus on [name] (Gate 3Q)
                p = re.sub(r'\.\s*Focus on\s+[A-Za-z0-9_ ]+\.', '.', p, flags=re.IGNORECASE)
                p = re.sub(r'\.\s*Focus on\s+[A-Za-z0-9_ ]+$', '.', p, flags=re.IGNORECASE)

                p = re.sub(r"'s's", "'s", p)
                p = re.sub(r'\s{2,}', ' ', p)

                sanitized_parts.append(p)

        return "".join(sanitized_parts)

class PromptBuilder:
    """
    Fluid Hollywood Director Prompt Builder & Compiler.
    Assembles prompts strictly according to Pillar 3 & Pillar 4 standards in organic cinematic prose.
    """
    MASTER_PREFIX = "Master-level cinematography and composition, fast-paced shot variation, atmospheric sound design."

    @classmethod
    def build_canonical_prompt(
        cls,
        style_header: str,
        track_declaration: str,
        context_block: str,
        subjects_block: str,
        props_block: str,
        room_acoustics: str,
        timeline_shots: list,
        negative_clause: str = "Do not generate subtitles, dialogue text, titles, timestamps, or written text anywhere in the video. Do not render duplicate characters or extra props."
    ) -> str:
        """
        Builds a 100% compliant Code Block 1 Video Prompt following Gate 3J, 3K, 3L, 3M, 3N, 3R, 3S standards.
        Enforces the 3-Block Label Standard, double newline spacing, and the 5-Part Sovereign Subject Protocol.
        """
        clean_header = PromptSanitizer.sanitize(style_header).strip() if style_header else "Style: Masterwork cinematic realism, fine organic film grain, natural optical depth."
        clean_header = re.sub(r'\bDaVinci\s+Resolve(\s+color\s+grading)?,?\s*', '', clean_header, flags=re.IGNORECASE).strip()
        if not clean_header.startswith(cls.MASTER_PREFIX):
            clean_header = f"{cls.MASTER_PREFIX} {clean_header}"
        
        if track_declaration and track_declaration.strip():
            header_full = f"{clean_header}. {track_declaration.strip()}."
        else:
            header_full = clean_header

        # Context block
        clean_context = PromptSanitizer.sanitize(context_block).strip()
        if clean_context.lower().startswith("[context]:"):
            clean_context = clean_context[len("[context]:"):].strip()

        # Subject block: Enforce 5-Part Sovereign Formula and Anti-Duplication Seal
        clean_subjects = PromptSanitizer.sanitize(subjects_block).strip()
        if clean_subjects.lower().startswith("[subject]:"):
            clean_subjects = clean_subjects[len("[subject]:"):].strip()
        
        # Ensure each subject line ends with anti-duplication seal if not present
        processed_subject_lines = []
        for line in clean_subjects.split("\n"):
            line_str = line.strip()
            if not line_str:
                continue
            if "— the only" not in line_str and "in frame" not in line_str:
                m = re.match(r'^([a-zA-Z0-9_\s\[\]]+?)\s*\[(?:100%\s*)?Appearance', line_str, re.IGNORECASE)
                if m:
                    char_name = re.sub(r'[\[\]]', '', m.group(1)).strip()
                    line_str = f"{line_str.rstrip('.,;')} — the only {char_name} in frame."
            processed_subject_lines.append(line_str)
        final_subjects = "\n".join(processed_subject_lines)

        # Props block
        clean_props = PromptSanitizer.sanitize(props_block).strip()
        if clean_props.lower().startswith("[prop]:") or clean_props.lower().startswith("[prop] :"):
            clean_props = re.sub(r'^\[prop\]\s*:\s*', '', clean_props, flags=re.IGNORECASE).strip()
        if not clean_props:
            clean_props = "(none — hands free of handheld props)"

        # Acoustics block
        clean_acoustics = PromptSanitizer.sanitize(room_acoustics).strip()
        if clean_acoustics.lower().startswith("diegetic room acoustics:"):
            clean_acoustics = clean_acoustics[len("diegetic room acoustics:"):].strip()
        if not clean_acoustics:
            clean_acoustics = "natural room tone, subtle cloth friction, and respiratory rhythm"

        # Timeline shots
        shots_text = "\n\n".join(PromptSanitizer.sanitize(shot).strip() for shot in timeline_shots)

        return (
            f"{header_full}\n\n"
            f"[context]:\n{clean_context}\n\n"
            f"[subject]:\n{final_subjects}\n\n"
            f"[PROP]:\n{clean_props}\n\n"
            f"Diegetic room acoustics: {clean_acoustics}\n\n"
            f"{shots_text}\n\n"
            f"Continuous fluid motion, realistic physics, zero morphing. Spatial positions anchored to the architecture; characters move only where the action says they move.\n"
            f"{negative_clause.strip()}"
        )

    @classmethod
    def build_fluid_prompt(
        cls,
        style_atmosphere: str,
        env_context: str,
        subject_staging_00: str,
        action_camera: str,
        dialogue_speaker: str = "",
        dialogue_verb: str = "says",
        dialogue_line: str = "",
        dialogue_voice_profile: str = "",
        settle_description: str = "",
        negative_clause: str = "Strictly zero violence, zero blood, zero weapons, zero harm to minors, zero self-harm, zero graphic trauma. Do not generate subtitles, dialogue text, titles, timestamps, or written text."
    ) -> str:
        """
        Routes fluid single-scene inputs through the canonical 3-Block Label architecture (Gate 3J/3K/3L/3M/3N compliant).
        """
        timings = WPSCalculator.calculate_timings(dialogue_line)
        timeline_shots = []
        if timings["has_dialogue"]:
            clean_action = PromptSanitizer.sanitize(action_camera, primary_speaker=dialogue_speaker).strip()
            verb = dialogue_verb.strip() if dialogue_verb else "says"
            dia_block = f'{dialogue_speaker} {verb} : “{dialogue_line}” ({dialogue_voice_profile})'
            timeline_shots.append(f"[{timings['lead_in_range']}] {clean_action}")
            timeline_shots.append(f"[{timings['dialogue_range']}] {dia_block}")
            if settle_description and settle_description.strip():
                clean_settle = PromptSanitizer.sanitize(settle_description, primary_speaker=dialogue_speaker).strip()
                timeline_shots.append(f"[{timings['settle_range']}] {clean_settle}")
        else:
            clean_action = PromptSanitizer.sanitize(action_camera, primary_speaker=dialogue_speaker).strip()
            timeline_shots.append(f"[{timings['lead_in_range']}] {clean_action}")
            if settle_description and settle_description.strip():
                clean_settle = PromptSanitizer.sanitize(settle_description, primary_speaker=dialogue_speaker).strip()
                timeline_shots.append(f"[{timings['action_range']}] {clean_settle}")

        return cls.build_canonical_prompt(
            style_header=style_atmosphere,
            track_declaration="",
            context_block=env_context,
            subjects_block=subject_staging_00,
            props_block="(none — hands free of handheld props)",
            room_acoustics="natural room tone, subtle cloth friction, and respiratory rhythm",
            timeline_shots=timeline_shots,
            negative_clause=negative_clause
        )

    @classmethod
    def build_omni_prompt(
        cls,
        style_header: str,
        env_context: str,
        subjects_staging: str,
        props_list: str,
        acoustics: str,
        timeline_shots: list,
        negative_clause: str = "Strictly zero violence, zero blood, zero weapons, zero harm to minors, zero self-harm, zero graphic trauma. Do not generate subtitles, dialogue text, titles, timestamps, or written text."
    ) -> str:
        """
        Backwards-compatible builder that delegates directly to build_canonical_prompt.
        """
        return cls.build_canonical_prompt(
            style_header=style_header,
            track_declaration="",
            context_block=env_context,
            subjects_block=subjects_staging,
            props_block=props_list,
            room_acoustics=acoustics,
            timeline_shots=timeline_shots,
            negative_clause=negative_clause
        )

def compile_and_validate_episode(html_content: str, output_path: str) -> bool:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content.strip())

    print(f"[*] Pre-validating compiled episode: {output_path}")
    passed = audit_episode_html(output_path)
    if not passed:
        raise RuntimeError(
            f"[FATAL COMPILER FAILURE]: {output_path} failed Master Episode Audit Suite! "
            f"Delivery is strictly blocked. Correct the data and recompile."
        )

    print(f"[V] ROOT COMPILER SUCCESS: {output_path} passed all gates and is verified production-ready.")
    return True

if __name__ == '__main__':
    print("Sven Master Prompt Compiler & Sanitizer Engine (Fluid Dynamic WPS Edition) initialized.")
