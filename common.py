import time
import logging



def delays(requests_limit, time_amount, requests_done=1):
    '''
    Generator of delays between requests to Facebook Graph API.

    Arguments:
    requests_limit - Maximum number of requests per time_amount.
    time_amount - The intervals request limiting works on.
    '''
    start = time.time()
    while True:
        request_num = requests_done
        requests_done += 1
        yield _count_delay(request_num, time.time() - start, requests_limit, time_amount)


def _count_delay(request_num, time_passed, requests_limit, time_amount):
    '''
    Count delay before following request to Graph API.
    '''
    max_frequency = requests_limit / time_amount
    if time_passed == 0:
        if request_num >= requests_limit:
            return time_amount
    else:
        if float(request_num + 1) / time_passed > max_frequency:
            next_time = float(request_num + 1) / max_frequency
            return next_time - time_passed    # Delay.
    return 0

def _call_and_retry(func, max_retries, *args, **kwargs):
    '''Calls `func` and retry on exception max_retries times.

    All the additional positional and keywork arguments are passed to func'''
    logger = logging.getLogger('root')
    global delays_gen
    for i in range(max_retries + 1):
        try:
            delay = delays_gen.next()
            logger.debug('Sleeping for %s seconds' % (delay))
            time.sleep(delay)
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(e)
            if i == max_retries:
                raise
            logger.debug('Retrying')
            time.sleep(5)

