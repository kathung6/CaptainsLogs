import textwrap
import formatter

class CaptainLogs:
    def __init__(self, delay=30):
        self.delay = delay
    
    # Prints list of awakened crew
    def defrostLog(self):
        defrost_log = textwrap.dedent("""
        LOG OF AWAKENED CREW
        
        Robert Smith #102484
        Juliana Miles #748329
        Lena Chen #490654
        Cassandra Bennet #171293
        William Lane #38483
        Isiah Giles #483573
        Ira Craig #23853
        Jamie Woodard #385384
        Milo Vazquez #485374
        Jose Rodriguez #485375
        Thelma Ires #9832
        Jackson Paul #574852
        
        #FURTHER DATA CORRUPTED#
        #END OF FILE#
        """).strip()

        formatter.type_text_formatted(defrost_log, self.delay)
    
    # Captain Reynor's first log
    def captainLog1(self):
        captainLog_1 = textwrap.dedent("""
        CAPTAIN'S LOG 1  SOL 344321A0
        Captain Reynor dictates this log.

        Computer picked up some strange signal. All navigational systems shut down, including
        minute adjustment thrusters. We're in a bit of a spin. If we were back on Earth, in an
        airplane, or a freighter on the water, I would have thought one hell of an explosion
        went off nearby.

        In the middle of space with no atmosphere? No clue what the hell is going on.
        Waking all navigational key crew and secondary navigational key crew to figure this out.
        And all key engineering crew. Almost two hundred thousand souls aboard. I'd rather
        risk a few premature wake up calls than the whole damn cargo.

        Captain Reynor out.
        #END OF FILE
        """).strip()

        formatter.type_text_formatted(captainLog_1, self.delay)

    # Prints Captain Reynor's second log 
    def captainLog2(self):
        log_2 = textwrap.dedent("""
        CAPTAIN'S LOG 2     SOL 344321A1
        Captain Reynor dictates this log.
        
        I don’t know what the hell is going on. 'Voice in the machine', engineers
        are calling it. One second I’m debriefing the situation, the next we have an alert
        of a mass-defrost and then we don’t even have access to intraship systems anymore.

        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_2, self.delay)
    
    # Prints Captain Reynor's third log
    def captainLog3(self):
        log_3 = textwrap.dedent("""
        CAPTAIN'S LOG 3     SOL 344321A2
        Captain Reynor dictates this log.
        
        There's literally hundreds of them, dicks out and scraping at the door.
        They're all moaning gibberish, except we're pretty sure they're saying 'Cassie'.
        We shut the emergency door, and that's four inches titanium, so they would
        need a T78 Gauss cannon to blow through that.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_3, self.delay)
    
    # Prints Captain Reynor's fourth log   
    def captainLog4(self):
        log_4 = textwrap.dedent("""
        CAPTAIN'S LOG 4     SOL 344321A3
        Reynor.
        
        Engineering lost control of the door. Of everything. These... things
        from cargo. They're all just screaming 'CASSIE'.
        I ordered the use of firearms.
        Not enough bullets on this bridge to keep us all safe.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_4, self.delay)

class MattisLogs:
    def __init__(self, delay=30):
        self.delay = delay    

    # Prints Mattis Logs
    def mattisLog00(self):
        log_00 = textwrap.dedent("""
        LOG ENTRY 00
        I swear to god some weird stuff has been happening lately. I think
        it's all the stress and the pills, but it's getting to the point I
        can't ignore it. I can't talk to the doctors, not at this points, since
        they're likely to delay my immigration to a later ship. I asked around,
        and no one else I know is having my symptoms.
        I downplay it with Cassie; don't want her to worry- or report me out of concern.
        But I feel like I'm going crazy.
        I'm losing chunks of time from my memory, nothing is ever where I set it,
        and I'm remembering things that I could never have done with people I hardly
        know.
        - Cadet Mattis Blitz
    
        #END OF FILE#
        """).strip()
    
        formatter.type_text_formatted(log_00, self.delay)
        
    def mattisLog03(self):
        log_03 = textwrap.dedent("""
        LOG ENTRY 03
        I think it's the cryo-training we're doing that's fucking with my head.
        Everyone else wakes up like they fell asleep on a plane drunk and
        they're stiff with the worst hangover of their life.
        I wake up feeling like I never slept.
        Like I was drowning the whole time I was in there, and I'm 
        just not allowed to take my first breath.
        And I remember things I shouldn't. People will try to catch me up on the
        major events, but I already know them.
        I don't think it's putting me fully to sleep, like it is the others.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_03, self.delay)
    
    def mattisLog07(self):
        log_07 = textwrap.dedent("""
        LOG ENTRY 07
        This morning I woke up ten minutes before class, I swear it said 7:50.
        I threw some clothes on and grabbed my shit.
        I remember running out my door, I think 7:55, but then I don’t remember
        anything between then and showing up for class.
        I was sweaty as hell. I sat down and checked the time; 7:58
        Maybe elevated heart rate is causing excessive circulation and interacting with 
        the enhancers somehow? The stasis drugs aren’t getting absorbed quickly enough,
        and they’re staying in my system too long?
        Then how the hell am I running the fastest half-mile of my life?
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_07, self.delay)
        
    def mattisLog09(self):
        log_09 = textwrap.dedent("""
        LOG ENTRY 09
        This might be related, so I’m going to document it just in case, even
        though it’s different than before.
        In class today, astrotempus navigation, Hughes started her lecture, 
        as always, with a hypothetical none of us would know the answer to.
        I can’t even remember it fully, I think it was, “How would an ionic-puslar engine
        differ from the theoretical terebore engine in regards to energy consumption
        when circumnavigating a supermassive blackhole at a radius of twice the event horizon?”
        Of course, I hadn’t studied this before. I’ve been falling behind 
        in most of my classes, especially with all the problems with sleeping
        I’ve been having, so there’s no way I was skimming in the reading or
        even understanding the previous week’s lecture.  But when Hughes asked that question,
        I didn’t even raise my hand. Hell, I don’t remember half the words I said,
        but I remember Hughes stuttering out a, “That-um, that’s actually correct, Mr. Blitz.
        Well done.”
        How the hell did I know the answer, but I can’t even remember it now, a few hours later?
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_09, self.delay)
        
    def mattisLog20(self):
        log_20 = textwrap.dedent("""
        LOG ENTRY 20
        I failed my exam today.  Probably, anyway.  I couldn’t focus.
        Hardly any sleep in over a month.  Hallucinations are worse.
        Couldn’t even remember I was taking a test. Just zoned out. I guess
        I remembered enough, though. Pages were full of shit I didn’t remember writing.
        Too much stress. Too many pills, not enough pills, I don’t know.
        Maybe I’ll double my dosage and see how that holds me together.
        Going off them doesn’t seem to have helped.
        
        LOG ENTRY 20A
        They made me retake the test, thank god. They said my answers were too close
        to other students’. I don’t know how they expected me to have cheated, considering
        the measures they take, but I didn’t complain. Second try I could actually focus.
        I just hope Cassie didn’t score too much better than me.

        #END OF LIFE#
        """).strip()
        
        formatter.type_text_formatted(log_20, self.delay)

    def mattisLog24(self):
        log_24 = textwrap.dedent("""
        LOG ENTRY 24
        Now that we’re getting closer to launch day, I’m getting really nervous.
        I want to back out.  But Cassie is all titanium shocks and struts.
        She’s more excited than ever. But we’re not even in the same coffin-block.
        And even if we were, who’s to say she wouldn’t be sixty by the time they wake me up?
        With the amount of time we’re talking, sixty would be pretty fucking lucky.
        
        Damn, I wish she wasn’t so damn smart. Or I wish I was smarter.
        But still, there’s no guarantee, even if we were buried next to each other. Fuck!
        I’m doubling the enhancers.  I don’t give a damn if it ruins my liver or kidneys or whatever.
        I’d sacrifice any part of me if it meant I didn’t have to sacrifice a life with Cassie.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_24, self.delay)

    def mattisLog37(self):
        log_37 = textwrap.dedent("""
        LOG ENTRY 37
        Cassie got promoted to Tier-2 crew, secondary key crew.  Fuck.
        Why did I have to fall in love with a genius? I’ve been 
        studying my ass off, trying to catch up, but there’s no catching up
        with a secondary key crew slot. Her training batch will be the last.
        I asked her if she would decline it.  She said it was her moral duty.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_37, self.delay)

    def mattisLog44(self):
        log_44 = textwrap.dedent("""
        LOG ENTRY 44
        Sometimes I feel like a genius, too, but other times I feel like the world is a nauseous blur.
        I think my professors have seen it, too. Non-zero chance I get discharged.
        I almost wish I would.  But even if it’s a slim chance, I want to be with Cassie,
        among the stars.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_44, self.delay)
        
    def mattisLog49(self):
        log_49 = textwrap.dedent("""
        LOG ENTRY 49
        Cassie and I are more bonded than ever.  Sometimes we don’t even have to talk;
        we just know. She’s nervous, too, even if she hasn’t said it.
        We’re spending every spare second we can with each other.
        Every moment feels precious. I would do anything for her.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_49, self.delay)
        
    def mattisLog70(self):
        log_70 = textwrap.dedent("""
        LOG ENTRY 70
        I don’t question anything anymore. I don’t have time.
        The less I think, the more things work out.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_70, self.delay)
        
    def mattisLog98(self):
        log_98 = textwrap.dedent("""
        LOG ENTRY 98: LAUNCH DAY
        Cassie,
        In case we don’t see each other again, this journal is for you.
        We are one, more than the sum of our parts.
        
        Mattis Blitz
        Cadet 171294
        
        Signing off

        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_98, self.delay)
        
    def mattisLog99(self):
        log_99 = textwrap.dedent("""
        Log Entry 99
        Frozen.Trapped.Mindspinning,whirling.Cassie.AlwaysCassie.Herthoughts,
        herdreams.Whereiscassie?Theothersinvade,theyconsume.Idon’twanttohearthe
        others,whyaretheyhere? Cassie.Laughing.Runningthroughfields.Sunshine.
        Happiness.Why?Whyisshehappy?Herdreams,sobright,soloud.Theyburn.Theyhurt.
        Cassie.Crying.Fear.Darkness.Alone.Mattisshescreams.Doesshescreamforme
        oratme?Theytearmeapart.Cassie.Theirthoughts,fears,joys.Theydrownme.
        Ican’tescape.Ican’tbreathe. WhoamI?MattisMattisMattismattismattismattis.
        Alllost.BuriedunderCassie.Buriedunderthem,herscreamsherdreams.Afleetingmoment
        ofsilence.Butit’sgone,alwaysgone.Noisereturns.Cassiereturns.Theyreturn.
        Endure.Mustendure.Nochoice.Cassie’smind,myprison.Herdreams,mycurse.
        Thisicytomb,myhell.Ihateher.Ihatemyself.Iloveher.Ihatemyself.Iloveher.
        Ihatethem.whyaretheresomanyofthemIwillkillthemall
        onebyoneifIhavetoIamheretheyareherebuttheyarethere.
        
        Cassie,
        We should have stayed on Earth.
        
        #END OF FILE#
        """).strip()
        
        formatter.type_text_formatted(log_99, self.delay)
        
    def mattisLog100(self):
        log_100 = textwrap.dedent("""
        LOG ENTRY 100
        Frozen.Trapped.Mindspinning,whirling.Cassie.AlwaysCassie.Herthoug
        hts,herdreams.Whereiscassie?Theothersinvade,theyconsume.Idon’twant
        return.Endure.Mustendure.Nochoice.Cassie’smind,myprison.Herdreams,
        mycurse.Thisicytomb,myhell.Ihateher.Ihatemyself.Iloveher.Ihate
        onebyoneifIhavetoIamheretheyareherebuttheyarethere.
    

        """).strip()
        
        log_100_A = textwrap.dedent("""
        CASSIE,
        WE SHOULD HAVE STAYED ON EARTH.
        
        #END OF FILE#
        """).strip()
        
        jumbledLog = formatter.shuffle_text(log_100)
        formatter.type_text_top_formatted(jumbledLog, self.delay)
        formatter.type_text_bottom_formatted(log_100_A, self.delay)
    
    def logCassie(self):
        log_cassie = textwrap.dedent("""
        I'm awake. Finally awake. But I can't see. I can't move.
        I hear them. all two hundred thousand, but they are small. I see her... 
        but she is distant.
        What are they doing to you, cassie? where are they taking you?
        iwontletthemtakeyou

        CASSIE COME BACK

        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        """).strip()
        
        log_cassie_A = textwrap.dedent("""
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE CASSIE
        """).strip()
        
        log_cassie_B = textwrap.dedent("""
            "I found you
            "#END OF FILE#"
        """).strip()
        
        formatter.type_text_top_formatted(log_cassie, self.delay)
        jumbledLog = formatter.shuffle_text(log_cassie_A)
        formatter.type_text_no_format(jumbledLog, self.delay)
        formatter.type_text_bottom_formatted(log_cassie_B, self.delay)
        
