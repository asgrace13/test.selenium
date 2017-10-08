# -*- coding: utf-8 -*-


def test_create_supply_agreement(app, json_agreements):
    agreement = json_agreements
    app.session.ensure_login(email=app.target["userEmail"], password=app.target["userPassword"])
    app.agreement.create(agreement)