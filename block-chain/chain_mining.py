# from apscheduler.schedulers.blocking import BlockingScheduler
# import logging
# import sys
# import utils
# import sync
# import constant as cnst
# import requests
#
# #BlockingScheduler: use when the scheduler is the only thing running in your process
# schedule = BlockingScheduler(standalone=True)
#
#
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#
# def mine_block(new_block, rounds,  stratingNonce):
#
#     none_range = [i+stratingNonce for i in range(rounds)]
#
#     for nonce in none_range:
#         new_block.nonce = nonce
#         new_block.calculate_hash()
#
#         if str(new_block.hash[0:cnst.DIFFICULTY]) == "0" * cnst.DIFFICULTY :
#             print(new_block.index, new_block.nonce)
#
#             assert new_block.is_valid()
#             return new_block, rounds, stratingNonce, new_block.timestamp
#
# def mine_from_previous_block(previous_block, stratingNonce, rounds, timeStamp):
#     new_block = utils.create_new_block_from_previous_block(previous_block=previous_block,
#                                                            timeStamp=timeStamp)
#
#     return mine_block(new_block, rounds, stratingNonce)
#
#
#
#
# def mine_for_block(blockChain,  rounds, stratingNonce, timestamp):
#     if not blockChain:
#         blockChain = sync.sync_local()
#
#     previous_block = blockChain.get_latest_block()
#
#     return mine_from_previous_block(previous_block, rounds, stratingNonce, timestamp)
#
#
# def broadcast_mined_block(new_block):
#     #  We want to hit the other peers saying that we mined a block
#     block_info_dict = new_block.__dict__
#     for peer in cnst.PEERS:
#         endpoint = "%s%s" % (peer[0], peer[1])
#         # see if we can broadcast it
#         try:
#             r = requests.post(peer + 'mined', json=block_info_dict)
#         except requests.exceptions.ConnectionError:
#             print("Peer %s not connected" % peer)
#             continue
#     return True
#
# def mine_for_block_listener(event):
#     # need to check if the finishing job is the mining
#     if event.job_id == 'mining':
#         new_block, rounds, stratingNonce, timeStamp = event.retval
#         # if didn't mine, new_block is None
#         # we'd use rounds and start_nonce to know what the next
#         # mining task should use
#         if new_block:
#             print("Mined a new block")
#             new_block.save()
#             broadcast_mined_block(new_block)
#             schedule.add_job(mine_from_previous_block, args=[new_block], kwargs={'rounds': cnst.STANDARD_ROUNDS, 'stratingNonce': 0},
#                           id='mining')  # add the block again
#         else:
#             print(event.retval)
#             schedule.add_job(mine_for_block,
#                           kwargs={'rounds': rounds, 'stratingNonce': start_nonce + rounds, 'timestamp': timestamp},
#                           id='mining')  # add the block again
#             schedule.print_jobs()
#
#
# if __name__=='__main__':
#     schedule.add_job(mine_for_block, kwargs={'rounds':cnst.STANDARD_ROUNDS,
#                                              'stratingNonce':0}, id='mining')
#
