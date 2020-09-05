import datetime

from django.db import models
from django.urls import reverse


class Data(models.Model):
    """Health Data Table."""

    SHIFT = (
        ("A", "AM"),
        ("P", "PM")
    )
    BOOLEAN_CHOICES = (
        ("Y", "Yes"),
        ("N", "No")
    )

    QUANTITY_CHOICES = (
        ("25", "25% or less"),
        ("50", "50% or less"),
        ("75", "75% or less"),
        ("100", "100% or less")
    )

    identifier = models.CharField(
        max_length=120, help_text="Data unique identifier"
    )
    # DAILY PROGRESS NOTE
    individual_name = models.CharField(
        max_length=120, help_text="Individual Name"
    )
    staff_name = models.CharField(max_length=120, help_text="Staff Name")
    date = models.DateTimeField(help_text="Date")
    shift = models.CharField(max_length=2, choices=SHIFT, help_text="Shift")
    diet = models.CharField(max_length=200, help_text="Diet")

    # MEAL INTAKE (BREAKFAST/LUNCH/DINNER)
    food_texture_choice = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, help_text="Yes/No"
    )
    food_texture_description = models.TextField(
        help_text="Did the individual tolerate food Texture"
    )
    food_texture1 = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, help_text="B"
    )
    food_texture2 = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, help_text="L"
    )
    food_texture3 = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, help_text="D"
    )
    quantity_consumed1 = models.CharField(
        max_length=3, choices=QUANTITY_CHOICES, help_text="25% or less"
    )
    quantity_consumed2 = models.CharField(
        max_length=3, choices=QUANTITY_CHOICES, help_text="50% or less"
    )
    quantity_consumed3 = models.CharField(
        max_length=3, choices=QUANTITY_CHOICES, help_text="75% or less"
    )
    consumed_explain = models.CharField(
        max_length=300, blank=True,
        help_text="If Consumed less than 75% Please Explain"
    )
    liked_unliked = models.CharField(
        max_length=300, blank=True,
        help_text="""What part of the meal did they like or did not like, if
        applicable?"""
    )
    incident_on_shift = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Has there been an incident involving this individual
        during your shift?"""
    )
    incident_on_shift_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    incident_report = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, blank=True,
        help_text="""If yes, has there been an incident report completed
        before the end of your shift?"""
    )
    incident_report_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    incident_behavior = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES, blank=True,
        help_text="""Did the individual display any behaviors during your
        shift not identified in the BSP?"""
    )
    incident_behavior_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )

    # MEDICAL CONCERN/MEDICAL APPOINTMENT
    observed_symptoms = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Do you observe any sign and symptoms of illness involving
        this individual during your shift?"""
    )
    observed_symptoms_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    medical_appointment = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Is there a medical appointment scheduled and completed
        during your shift?"""
    )
    medical_appointment_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    home_or_job = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Is the individual home from the day program or from their
        job?"""
    )
    home_or_job_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    side_effects = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Are there any observable signs/symptoms of side effects
        of medication(s)?"""
    )
    side_effects_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    adaptive_equipment = models.CharField(
        max_length=300, help_text="List the adaptive equipment:"
    )
    equipment_concern = models.CharField(
        max_length=300, blank=True,
        help_text="Any concerns with equipment, if so explain:"
    )

    # PROGRAM ACTIVITIES
    program_implemented = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Is all programs implemented as outlined?"""
    )
    program_documented = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="""Is Program Documentation completed as outlined?"""
    )
    finance_discussion = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="Discussion of Finance?"
    )
    finance_discussion_explain = models.CharField(
        max_length=300, help_text="Explain", blank=True
    )
    home_visitor = models.CharField(
        max_length=2, choices=BOOLEAN_CHOICES,
        help_text="Is there a visitor in the home during your shift?"
    )

    # DIRECT SUPPORT STAFF – PROGRESS NOTES
    summary1_date = models.DateTimeField(help_text="Date/Time")
    summary1_initial = models.CharField(
        max_length=120, help_text="Staff Initial"
    )
    summary1 = models.TextField(help_text="First Summary")
    summary2_date = models.DateTimeField(help_text="Date/Time")
    summary2_initial = models.CharField(
        max_length=120, help_text="Staff Initial"
    )
    summary2 = models.TextField(help_text="Second Summary")
    summary3_date = models.DateTimeField(help_text="Date/Time")
    summary3_initial = models.CharField(
        max_length=120, help_text="Staff Initial"
    )
    summary3 = models.TextField(help_text="Third Summary")
    summary4_date = models.DateTimeField(
        help_text="Date/Time", blank=True, null=True
    )
    summary4_initial = models.CharField(
        max_length=120, help_text="Staff Initial", blank=True
    )
    summary4 = models.TextField(help_text="Fourth Summary", blank=True)
    residential_manager_review = models.CharField(
        max_length=300, help_text="Residential Manager Review"
    )

    def save(self, *args, **kwargs):
        """Compute identifier field before saving."""
        self.identifier = self.individual_name + " " + self.date.strftime(
            "%a-%m-%Y %I:%M %p"
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.identifier

    def get_absolute_url(self):
        """Return objects unique URL."""
        return reverse('data-view', kwargs={'pk': self.pk})
