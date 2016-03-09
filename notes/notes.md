

    $ pylint --generate-rcfile > ~/.pylintrc    # sample rc file
    $ vi ~/.pylintrc
    disable=line-too-long, invalid-name


pay monthly button inactive:

    <li class="btn_arrow_tab left inactive">
        <a href="#" class="doubleText">Pay Monthly <small>View standard rates and Bolt Ons</small>
        </a>
    </li>

active:

    <li class="btn_arrow_tab left active  ui-state-default ui-corner-top">
        <a href="#paymonthlyTariffPlan" id="paymonthly" class="doubleText">Pay Monthly<small>View standard rates and Bolt Ons</small></a>
    </li>