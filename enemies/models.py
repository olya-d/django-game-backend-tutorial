from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_fsm import FSMIntegerField, transition, can_proceed


class Monster(models.Model):
    WANDERING = 10
    ATTACKING = 20
    LOOKING_FOR_AID = 30
    EVADING = 40

    STATES = (
        (WANDERING, 'wandering'),
        (ATTACKING, 'attacking'),
        (LOOKING_FOR_AID, 'looking_for_aid'),
        (EVADING, 'evading')
    )

    state = FSMIntegerField(default=WANDERING, choices=STATES)
    user_being_attacked = models.ForeignKey(User, default=None, null=True)
    health_points = models.IntegerField(default=10)

    def health_is_low(self):
        return self.health_points <= 5

    @transition(field=state,
                source=[WANDERING],
                target=ATTACKING)
    def attack(self, user):
        self.user_being_attacked = user
        self.save()
        print('Attacking user')

    @transition(field=state,
                source=[ATTACKING, LOOKING_FOR_AID],
                target=WANDERING)
    def wander(self):
        self.user_being_attacked = None
        self.save()
        print('Just wandering')

    @transition(field=state,
                source=[ATTACKING],
                target=EVADING)
    def evade(self):
        pass

    @transition(field=state,
                source=[EVADING],
                target=LOOKING_FOR_AID,
                conditions=[health_is_low])
    def look_for_aid(self):
        print('Looking for aid')


@receiver(signals.post_save, sender=Monster)
def post_save_callback(sender, **kwargs):
    monster = kwargs['instance']
    if can_proceed(monster.look_for_aid):
        monster.look_for_aid()
        monster.save()
