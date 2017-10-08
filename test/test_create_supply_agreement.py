# -*- coding: utf-8 -*-


def test_create_supply_agreement(app, json_agreements):
    agreement = json_agreements
    app.agreement.create(agreement)