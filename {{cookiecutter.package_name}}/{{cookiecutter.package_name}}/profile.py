import sqlite3
import urllib

import requests
from munibot.config import config
from munibot.profiles.base import BaseProfile


class {{cookiecutter.class_name}}(BaseProfile):
    """
    A Munibot profile for tweeting images of {{cookiecutter.admin_divisions}}
    """

    # Mandatory properties

    """
    A unique identifier for the profile, that will be used when running the
    commands and on the configuration file.
    """
    id = "{{cookiecutter.bot_id}}"

    """
    A longer description of the profile.
    """
    desc = "{{cookiecutter.bot_name}}"

    # Mandatory hooks

    """
    Given a feature id, returns a tuple with the extent and the geometry of the
    the boundaries of the feature.

    The extent is a tuple containing (minx, miny, maxx, maxy). The geometry is
    a dict containing the geometry in GeoJSON format.
    """

    def get_boundaries(self, id_):

        raise NotImplementedError

    """
    Returns a base image for the given extent (minx, miny, maxx, maxy).

    The return value is a file-like object containing the raster image for the
    provided extent.
    """

    def get_base_image(self, extent):

        raise NotImplementedError

    """
    Returns the text that needs to be included in the tweet for this particular
    feature.
    """

    def get_text(self, id_):

        raise NotImplementedError

    """
    Returns the id of the next feature that should be tweeted.

    This is used if the ``munibot tweet`` command is called withot providing
    an id.
    """

    def get_next_id(self):

        raise NotImplementedError

    # Optional hooks

    """
    Return a tuple with the longitude and latitude that should be associated
    with the tweet.

    The bot account should have location information on tweets activated.
    """

    def get_lon_lat(self, id_):

        pass

    """
    Function that will be called after sending the tweet, that will receive
    the feature and the status id of the tweet sent.
    """

    def after_tweet(self, id_, status_id):

        pass
